import jwt
import datetime
from flask import Blueprint, request, jsonify
from services.store_user_service import create_store_user, authenticate_store_user
from models.database import db

store_user_bp = Blueprint('store_user_bp', __name__)

import os
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

@store_user_bp.route('/store_user/signup', methods=['POST'])
def signup_store_user():
    data = request.get_json()
    result = create_store_user(data)
    return jsonify(result), 201 if result['success'] else 400

# http://127.0.0.1:5000/api/store_user/signup

@store_user_bp.route('/store_user/login', methods=['POST'])
def login_store_user():
    data = request.get_json()
    email_id = data.get('email_id')
    password = data.get('password')
    result = authenticate_store_user(email_id, password)
    if result['success']:
        message="store user logged in successful ('below the token copy and paste it on the headers and update rate of the product')"         
        token = jwt.encode({
            'email_id': email_id,
            'role': result['role'],  # Include the user role in the token payload
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({"message":message,'token': token}), 200
    return jsonify(result), 401

# http://127.0.0.1:5000/api/store_user/login