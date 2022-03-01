import flask
from flask import request
import pymongo
import jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://admin:beckrekekre@cluster0.uc4dj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", server_api=ServerApi('1'))

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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

    results = collection.find({"time":time})

#    return f"station name is {station}, the time is {time}, and the filters added are {filters}"

    for result in results:
        return jsonify(result.to_json())


app.run()
