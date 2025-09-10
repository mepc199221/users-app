from flask import Flask
from flask_cors import CORS
from routes.user_email_search import product_search


app = Flask(__name__)
CORS(app)


app.register_blueprint(product_search, url_prefix ='/user')


@app.route('/')
def index():
    return jsonify ({"data":"user-app"})

if __name__ == "__main__":
    app.run(debug=True)

