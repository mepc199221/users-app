import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
from mock import usuarios
user_delete = Blueprint('user_delete', __name__)

@app.route('/user/delete', methods=['DELETE'])
def fn_delete_user_by_email(user_email):
    if request.method == 'DELETE':
        res = _search_user_by_email(user_email)
    
        usuarios.remove(res)
    
        return jsonify({
            "data":"delete success"
        })
def _search_user_by_email(email):
    for user in usuarios:
        if user['email'] == int(email):
           return user
        return None