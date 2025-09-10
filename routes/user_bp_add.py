import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
from mock import usuarios


user_bp_add = Blueprint('user_bp_app', __name__)



@user_bp_add.route('/add', methods=['POST'])
def fn_add_new_user():
    if request.method == 'POST':
        req = request.json

        new_user = _model_user_swap(req) 
  
        usuarios.append(new_user)
    
        return jsonify({
            "data":new_user
        })   
    



def _model_user_swap(req):
    return  {
        "id":_generate_new_id_user(),
        "nombre": req['nombre'],
        "precio": req['precio'],
        "pantalla": req['pantalla'],
        "bateria": req['bateria'],
        "almacenamiento": req['almacenamiento']
    }


def _generate_new_id_user():
    global next_id
    cache = next_id
    next_id += 1
    return cache