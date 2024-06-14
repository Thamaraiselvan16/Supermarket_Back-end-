# app/models/store_user.py
from models.database import db
from werkzeug.security import generate_password_hash

class StoreUser(db.Model):
    __tablename__ = 'store_user'

    store_user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    sex = db.Column(db.Enum('Male', 'Female', 'Other'))
    contact_number = db.Column(db.String(15))
    email_id = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    designation = db.Column(db.Enum('Manager', 'Sales Man'))

    def __init__(self, first_name, last_name, age, sex, contact_number, email_id, password, designation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.contact_number = contact_number
        self.email_id = email_id
        self.password = generate_password_hash(password)
        self.designation = designation

    def to_dict(self):
        return {
            'store_user_id': self.store_user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'sex': self.sex,
            'contact_number': self.contact_number,
            'email_id': self.email_id,
            'designation': self.designation
        }
