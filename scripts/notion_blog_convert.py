import requests, json
import os
from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Jinja template setup
env = Environment(
    loader=FileSystemLoader("./scripts/templates"),
    autoescape=select_autoescape()
)
template = env.get_template("post.md.j2")

# Read exported datas
with open('./full-properties.json', 'r', encoding='utf8') as f:
    data = json.load(f)

# Data structure
class BlogParsingError:
    msg: str
    link: str

    def __init__(self, link, msg):
        self.msg = msg
        self.link = link
        print(msg)

class BlogItem:
    """Class for keeping track blog post"""
    title: str
    slug: str
    date: str
    image: str
    description: str
    categories: list[str]
    tags: list[str]
    draft: bool
    post_type: str

    def from_notion(self, item):
        errors = []

        self.title = item["properties"]["Name"]["title"][0]["text"]["content"]
        self.slug = item["url"].replace("https://www.notion.so/", "")
        
        if item["properties"]["Published Date"]["date"] is not None:
            self.data  = item["properties"]["Published Date"]["date"]["start"]
        else:
            errors.append(BlogParsingError(
                item['url'],
                f"Missing Published Date for: {self.title}"
            ))
        
        if item["cover"] is not None:
            self.image = item["cover"]
        else:
            errors.append(BlogParsingError(
                item['url'],
                f"Missing cover for: {self.title}"
            ))

        if item["cover"] is not None:
            self.image = item["cover"]
        else:
            errors.append(BlogParsingError(
                item['url'],
                f"Missing cover for: {self.title}"
            ))

        if len(item["properties"]["Description"]["rich_text"]) > 0:
            self.description = item["properties"]["Description"]["rich_text"][0]["text"]["content"]
        else:
            errors.append(BlogParsingError(
                item['url'],
                f"Missing description for: {self.title}"
            ))

        if len(item["properties"]["🟣 Resources"]["relation"]) > 0:
            self.categories = [r["id"] for r in item["properties"]["🟣 Resources"]["relation"]]
        else:
            errors.append(BlogParsingError(
                item['url'],
                f"Missing categories for: {self.title}"
            ))

        self.tags = item["properties"]["Tags"]["multi_select"]

        self.draft = True
        self.post_type = "post"

        return self, errors

# perform transformatiom
all_errors = []
for item in data["results"]:
    post, errors = BlogItem().from_notion(item)
    all_errors.extend(errors)
    parsed_template =template.render(post.__dict__)

    with open(f"./website/content/blog/{post.slug}.md", "w") as f:
        f.write(parsed_template)
    
# handle errors
# print([i.__dict__ for i in all_errors])