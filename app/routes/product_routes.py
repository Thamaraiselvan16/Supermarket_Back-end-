# app/routes/product_routes.py
from flask import Blueprint, request, jsonify
from models.products import Products
from services.product_service import add_product, delete_product
from utils.decorators import manager_required
from models.database import db

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/product', methods=['POST'])
@manager_required
def add_new_product():
    data = request.get_json()
    result = add_product(data)
    return jsonify(result), 201 if result['success'] else 400

# http://127.0.0.1:5000/api/product
# in headers
# Content-Type: application/json
# Authorization: Bearer <your_jwt_token>

@product_bp.route('/product/<int:product_id>', methods=['PUT'])
@manager_required
def update_product(product_id):
    data = request.get_json()
    product = Products.query.get(product_id)
    if not product:
        return jsonify({'message': 'Sorry, Product is not found', 'success': False}), 404

    product.rate = data.get('rate', product.rate)
    db.session.commit()

    return jsonify({'message': 'Product updated successfully', 'success': True}), 200

# http://127.0.0.1:5000/api/product/3
# in headers
# Content-Type: application/json
# Authorization: Bearer <your_jwt_token>

@product_bp.route('/product/<int:product_id>', methods=['DELETE'])
@manager_required
def remove_product(product_id):
    result = delete_product(product_id)
    return jsonify(result), 200 if result['success'] else 400

# http://127.0.0.1:5000/api/product/1
# in headers
# Content-Type: application/json
# Authorization: Bearer <your_jwt_token>