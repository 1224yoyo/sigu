from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client
import os

app = Flask(__name__)
CORS(app)

supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_KEY"]
)


@app.route("/api/hello")
def hello():
    print(555)
    return jsonify({"msg": "Hello Render"})
    

@app.route("/api/send", methods=["POST"])
def send():
    data = request.json
    supabase.table("chat").insert({
        "name": data["name"],
        "text": data["text"]
    }).execute()
    return jsonify({"ok": True})

@app.route("/api/list")
def list_msg():
    res = supabase.table("chat").select("*").order("id").execute()
    return jsonify(res.data)
