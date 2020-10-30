from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import data
import redis
from rq import Queue
from data import edit 
from worker import conn


# Create an instance of Flask
app = Flask(__name__)


q=Queue(connection=Conn)


# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    # Find one record of data from the mongo database
    # Return template and data
    return render_template("index.html")


@app.route("/twitter_data")
def twitter_data():
    result = q.enqueue(edit, 'http://heroku.com')
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)