from bs4 import BeautifulSoup
import pandas as pd
import requests, json
from collections import defaultdict
from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb://localhost:27017/")
db = client["scrap"]
collection = db["data"]

def get_mdata():
    try:
        data = list(collection.find())
        for doc in data:
            if "_id" in doc and isinstance(doc["_id"], ObjectId):
                doc["_id"] = str(doc["_id"])
        return data if data else "no data found"
    except Exception as e:
        return {"error": str(e)}

def scrape_file(file):
    try:
        df = pd.read_csv(file)
        print("DataFrame loaded:")
        print(df)
        df1 = json.loads(df.to_json(orient='records'))
        print("First record in JSON format:")
        print(df1[0])
        return df1 if df1 else "No data found in file."
    except Exception as e:
        return f"Error processing file: {str(e)}"



def scrape_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        tag_dict = defaultdict(list)

        for tag in soup.find_all(True):
            text = tag.get_text(strip=True)
            if text:
                tag_dict[tag.name].append(text)

        result_dict = dict(tag_dict)
        collection.insert_one(result_dict)

        return result_dict
    except Exception as e:
        return f"Error scraping URL: {str(e)}"
