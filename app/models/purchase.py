# app/models/purchase.py
from models.database import db

class Purchase(db.Model):
    __tablename__ = 'Purchase'
    purchase_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User_details.user_id'))
    email_id = db.Column(db.String(100), db.ForeignKey('User_details.email_id'))
    item = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    rate = db.Column(db.Numeric(10, 2))
    date_of_purchase = db.Column(db.Date)
