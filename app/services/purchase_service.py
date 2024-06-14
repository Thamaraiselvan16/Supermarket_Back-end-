# app/services/purchase_service.py
from models.database import db
from models.purchase import Purchase
from models.products import Products
from models.user_details import UserDetails
from datetime import datetime, timedelta

def create_purchase(data):
    user = UserDetails.query.filter_by(email_id=data['email_id']).first()
    if not user:
        return {'success': False, 'message': 'User not found'}

    product = Products.query.filter_by(product_name=data['item']).first()  # Check if the item exists
    if not product:
        return {'success': False, 'message': 'Item not found'}

    new_purchase = Purchase(
        user_id=user.user_id,
        email_id=user.email_id,
        item=data['item'],
        quantity=data['quantity'],
        rate=data['rate'],
        date_of_purchase=datetime.strptime(data['date_of_purchase'], '%Y-%m-%d')
    )
    db.session.add(new_purchase)
    db.session.commit()
    return {'success': True, 'message': 'Purchase recorded successfully'}

def get_total_items_in_date_range(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    total_items = db.session.query(db.func.sum(Purchase.quantity)).filter(
        Purchase.date_of_purchase.between(start_date, end_date)
    ).scalar()
    return {'total_items': total_items if total_items else 0}

def get_users_with_high_purchases():
    results = db.session.query(
        UserDetails.first_name,
        UserDetails.last_name,
        db.func.sum(Purchase.quantity * Purchase.rate).label('total_amount')
    ).join(Purchase, UserDetails.user_id == Purchase.user_id
    ).group_by(UserDetails.user_id, Purchase.date_of_purchase
    ).having(db.func.sum(Purchase.quantity * Purchase.rate) > 1000
    ).all()

    return [
        {
            'first_name': result.first_name,
            'last_name': result.last_name,
            'total_amount': float(result.total_amount)
        }
        for result in results
    ]

def get_total_sales_shampoo_last_7_days():
    seven_days_ago = datetime.now() - timedelta(days=7)
    total_sales = db.session.query(
        db.func.sum(Purchase.quantity * Purchase.rate)
    ).filter(
        Purchase.item == 'Shampoo',
        Purchase.date_of_purchase >= seven_days_ago
    ).scalar()
    return {'total_sales_shampoo': total_sales if total_sales else 0}


def get_daily_sales():
    today = datetime.now().date()
    sales = db.session.query(Purchase.item, db.func.sum(Purchase.quantity).label('QTY'), db.func.sum(Purchase.quantity * Purchase.rate).label('Amount')).filter(
        Purchase.date_of_purchase == today
    ).group_by(Purchase.item).all()
    
    return {item: {'QTY': qty, 'Amount': float(amount)} for item, qty, amount in sales}

def get_weekly_sales():
    week_start = datetime.now().date() - timedelta(days=datetime.now().date().weekday())
    week_end = week_start + timedelta(days=6)
    sales = db.session.query(Purchase.item, db.func.sum(Purchase.quantity).label('QTY'), db.func.sum(Purchase.quantity * Purchase.rate).label('Amount')).filter(
        Purchase.date_of_purchase.between(week_start, week_end)
    ).group_by(Purchase.item).all()
    
    return {item: {'QTY': qty, 'Amount': float(amount)} for item, qty, amount in sales}


def get_total_sales_in_date_range(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    sales_data = db.session.query(
        Purchase.item,
        db.func.sum(Purchase.quantity).label('QTY'),
        db.func.sum(Purchase.quantity * Purchase.rate).label('Amount')
    ).filter(
        Purchase.date_of_purchase.between(start_date, end_date)
    ).group_by(Purchase.item).all()
    
    return {sale.item: {'QTY': sale.QTY, 'Amount': sale.Amount} for sale in sales_data}
