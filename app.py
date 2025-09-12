from flask import Flask, jsonify
from flask_cors import CORS
from routes.user_list import user_list
from routes.user_email_search import product_search

app = Flask(__name__)
CORS(app)


app.register_blueprint(product_search, url_prefix ='/user')
app.register_blueprint(user_list, url_prefix='/users')

@app.route('/')
def index():
    return jsonify ({"data":"user-app"})

@app.errorhandler(404)
def handle_404(e):
response = {
"error": "Not Found",
"message": "La ruta solicitada no existe fuera de aqui mi loco",
"status": 404
}
return jsonify(response), 404

if __name__ == "__main__":
    app.run(debug=True)

