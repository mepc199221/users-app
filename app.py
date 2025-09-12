from flask import Flask, jsonify
from flask_cors import CORS
from routes.user_list import user_list
from routes.user_email_search import product_search
from routes.name_search import name_search

app = Flask(__name__)
CORS(app)


app.register_blueprint(product_search, url_prefix ='/user')
app.register_blueprint(user_list, url_prefix='/users')
app.register_blueprint(name_search, url_prefix='/search')

@app.route('/')
def index():
    return jsonify ({"data":"user-app"})

if __name__ == "__main__":
    app.run(debug=True)