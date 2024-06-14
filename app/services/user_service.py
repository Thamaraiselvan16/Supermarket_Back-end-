# app/services/user_service.py

from models.database import db
from models.user_details import UserDetails
from passlib.hash import bcrypt

def create_user(data):
    hashed_password = bcrypt.hash(data['password'])
    new_user = UserDetails(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        sex=data['sex'],
        contact_number=data['contact_number'],
        email_id=data['email_id'],
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(email, password):
    user = UserDetails.query.filter_by(email_id=email).first()
    if user and bcrypt.verify(password, user.password):
        return user
    return None
