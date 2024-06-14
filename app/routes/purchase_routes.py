# app/routes/purchase_routes.py
from flask import Blueprint, request, jsonify
from services.purchase_service import create_purchase, get_total_sales_shampoo_last_7_days,get_users_with_high_purchases, get_total_items_in_date_range

purchase_bp = Blueprint('purchase_bp', __name__)

@purchase_bp.route('/purchase', methods=['POST'])
def purchase():
    data = request.get_json()
    result = create_purchase(data)
    return jsonify(result), 201 if result['success'] else 400

# http://127.0.0.1:5000/api/purchase

@purchase_bp.route('/total_items', methods=['GET'])
def get_total_items():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    if not start_date or not end_date:
        return jsonify({'success': False, 'message': 'Please give correct start_date and end_date, this is are required (e.x: yyyy-mm-dd)'}), 400
    
    total_items = get_total_items_in_date_range(start_date, end_date)
    return jsonify(total_items), 200

# example endpoint
# http://127.0.0.1:5000/api/total_items?start_date=2024-06-10&end_date=2024-06-13

@purchase_bp.route('/high_purchases', methods=['GET'])
def high_purchases():
    users = get_users_with_high_purchases()
    return jsonify(users), 200

# example endpoint
# http://127.0.0.1:5000/api/high_purchases

@purchase_bp.route('/shampoo_sales', methods=['GET'])
def shampoo_sales():
    total_sales = get_total_sales_shampoo_last_7_days()
    return jsonify(total_sales), 200

# example endpoint
# http://127.0.0.1:5000/api/shampoo_sales