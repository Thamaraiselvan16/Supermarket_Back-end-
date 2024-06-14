from models.database import db


class Products(db.Model):
    __tablename__ = 'Products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    rate = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer)
    
    def __init__(self, product_name, rate, stock):
        self.product_name = product_name
        self.rate = rate
        self.stock = stock