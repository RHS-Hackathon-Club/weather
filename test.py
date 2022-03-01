#!/usr/bin/env python
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://admin:beckrekekre@cluster0.uc4dj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = client.weather
collection = db.data

results = db.data.find_one({"station":0})
print(type(results))

