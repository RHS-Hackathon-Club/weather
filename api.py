import flask
from flask import request, send_from_directory, jsonify
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.json_util import *

app = flask.Flask(__name__)
app.config["DEBUG"] = False

client = MongoClient("mongodb+srv://admin:beckrekekre@cluster0.uc4dj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = client.weather
collection = db.data

@app.route('/', methods=['GET'])
def home():
    with open('index.html') as f:
        return f.read()

@app.route('/js/<path:path>', methods=['GET'])
def send_js(path):
    return send_from_directory('js', path)

#@app.errorhandler(404)
#def not_found(e):
#    return "refer to hedgedoc for site/api usage"

@app.route('/api/data')
def page():
    station = int(request.args['station'])
    time = int(request.args['time'])

    results = []

    for result in list(collection.find({"station":station})):
        if result["time"] >= time:
            del result["_id"]
            results.append(result)
    
    return jsonify(results)

app.run()