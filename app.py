from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify ({"data":"user-app"})

if __name__ == "__main__":
    app.run(debug=True)