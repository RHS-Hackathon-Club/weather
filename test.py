import time
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://admin:beckrekekre@cluster0.uc4dj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = client.weather
print(db)
dummy = db.dummy

while True:
    dummy.insert_one({"time":time.time(), "beckre":"kekre"})
