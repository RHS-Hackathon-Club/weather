import flask
from flask import request
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_pymongo import PyMongo
from bson.json_util import *

app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:beckrekekre@cluster0.uc4dj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
app.config["DEBUG"] = True

client = MongoClient("mongodb+srv://admin:beckrekekre@cluster0.uc4dj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))

mongo = PyMongo(app)

db = client.weather
collection = db.data

@app.route('/', methods=['GET'])
def home():
    return "welcome home, big bro!"

@app.route('/api/data')
def page():
    station = request.args['station']
    time = request.args['time']
    filters = request.args['filters']
    results = list(collection.find({"station":station}))

    return str(loads(dumps(list(collection.find({"station":0})))))

    #return f"station name is {station}, the time is {time}, and the filters added are {filters}"

app.run()
