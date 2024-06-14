from models.database import db


class UserDetails(db.Model):
    __tablename__ = 'User_details'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    sex = db.Column(db.Enum('Male', 'Female', 'Other'))
    contact_number = db.Column(db.String(15))
    email_id = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))