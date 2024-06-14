# app/utils/decorators.py

from functools import wraps
from flask import request, jsonify
import jwt

import os
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

def manager_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]  # Extract (token part)

        if not token:
            return jsonify({'message': 'Token is missing', 'success': False}), 403

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            if data['role'] != 'Manager':
                return jsonify({'message': 'Manager access required', 'success': False}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired', 'success': False}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token', 'success': False}), 403

        return f(*args, **kwargs)
    return decorated_function