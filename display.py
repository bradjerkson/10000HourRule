import sys
import logic
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def default():
    return "API Server: connection successful"

@app.route("/get/<username>")
def generate_results(username):
    


if __name__ == "__main__":
    app.run(host="0.0.0.0")
