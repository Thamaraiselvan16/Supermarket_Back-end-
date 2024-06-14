# app/services/product_service.py
from models.database import db
from models.products import Products

def add_product(data):
    new_product = Products(
        product_name=data['product_name'],
        rate=data['rate'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return {'success': True, 'message': 'Product added successfully'}

def delete_product(product_id):
    product = Products.query.filter_by(product_id=product_id).first()
    if product:
        db.session.delete(product)
        db.session.commit()
        return {'success': True, 'message': 'Product deleted successfully'}
    else:
        return {'success': False, 'message': 'Product not found'}

def update_product_rate(product_id, rate):
    product = Products.query.filter_by(product_id=product_id).first()
    if product:
        product.rate = rate
        db.session.commit()
        return {'success': True, 'message': 'Product rate updated successfully'}
    else:
        return {'success': False, 'message': 'Product not found'}
