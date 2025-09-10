from flask import Flask
from flask_cors import CORS
from routes.user_name_and_email_search import user_bp

app = Flask(__name__)
CORS(app)


app.register_blueprint(user_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)