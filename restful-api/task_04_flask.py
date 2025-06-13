#!/usr/bin/python3
"""
task_04_flask.py
"""
import jsonify
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))

@app.route("status")
def status():
    return("OK")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

