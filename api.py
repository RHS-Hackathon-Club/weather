import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "welcome home, big bro!"

@app.route('/api/data')
def page():
    time = request.args['time']
    filters = request.args['filters']
    return f"the time is {time}, and the filters added are {filters}"

app.run()
