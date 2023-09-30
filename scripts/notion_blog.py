import requests, json
import os
from dataclasses import dataclass

token = os.environ["NOTION_TOKEN"]
databaseID = os.environ["NOTION_DB_ID"]
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.post(readUrl, headers=headers)
    data = res.json()
    print(readUrl, res.status_code)

    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return data

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
        self.title = item["properties"]["Name"]["title"][0]["text"]["content"]
        
        if item["properties"]["Published Date"]["date"] is not None:
            self.data  = item["properties"]["Published Date"]["date"]["start"]
        else:
            print(f"Missing Published Date for {self.title}")
        
        if item["cover"] is not None:
            self.image = item["cover"]
        else:
            print(f"Missing cover for {self.title}")

        return self

db = readDatabase(databaseID, headers)
for item in db["results"]:
    post = BlogItem().from_notion(item)
    print(post.__dict__)

