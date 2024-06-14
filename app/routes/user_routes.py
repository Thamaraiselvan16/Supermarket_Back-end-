# app/routes/user_routes.py

from flask import Blueprint, request, jsonify
from services.user_service import create_user, authenticate_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    user = create_user(data)
    if user:
        return jsonify({'message': 'User created successfully'}), 201

# http://127.0.0.1:5000/api/user/signup

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = authenticate_user(data['email_id'], data['password'])
    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# http://127.0.0.1:5000/api/user/login