from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/api/hello")
def hello():
    return jsonify({"msg": "Hello Render"})

if __name__ == "__main__":
    app.run()
