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

db = readDatabase(databaseID, headers)
