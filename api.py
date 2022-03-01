import flask
from flask import request
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.json_util import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

client = MongoClient("mongodb+srv://admin:beckrekekre@cluster0.uc4dj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = client.weather
collection = db.data

@app.route('/', methods=['GET'])
def home():
    return "refer to hedgedoc for api path"

@app.errorhandler(404)
def not_found(e):
    return "refer to hedgedoc for api usage"

@app.route('/api/data')
def page():
    station = int(request.args['station'])
    time = int(request.args['time'])

    results = []

    for result in list(collection.find({"station":station})):
        if result["time"] >= time:
            results.append(result)
    
    return str(loads(dumps(results)))

app.run()
