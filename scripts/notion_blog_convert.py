import requests, json
import os
from dataclasses import dataclass

with open('./full-properties.json', 'r', encoding='utf8') as f:
    data = json.load(f)

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
    date: str
    image: str
    description: str
    categories: list[str]
    tags: list[str]
    draft: bool = False
    type: str = "post"

    def from_notion(self, item):
        errors = []

        self.title = item["properties"]["Name"]["title"][0]["text"]["content"]
        
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

        return self, errors


all_errors = []
for item in data["results"]:
    post, errors = BlogItem().from_notion(item)
    all_errors.extend(errors)
    print(post.__dict__)
    

print([i.__dict__ for i in all_errors])