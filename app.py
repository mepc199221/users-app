from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.user_list import user_list
app = Flask(__name__)

app.register_blueprint(user_list, url_prefix='/users')

@app.route('/')
def index():
    return jsonify ({"data":"user-app"})

if __name__ == "__main__":
    app.run(debug=True)