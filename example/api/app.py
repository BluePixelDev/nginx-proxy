from flask import Flask, jsonify
from dotenv import load_dotenv
import requests
import os

load_dotenv()
NASA_API_KEY = os.environ["NASA_API_KEY"]

app = Flask(__name__)

@app.route("/apod")
def daily_image():
    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&thumbs=true")
    return r.json()

@app.route("/hello")
def hello():
    data = {
        "message": "Hello World"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()