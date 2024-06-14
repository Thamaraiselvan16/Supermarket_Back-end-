# app/services/store_user_service.py
from models.store_user import StoreUser
from models.database import db
from werkzeug.security import check_password_hash

def create_store_user(data):
    new_user = StoreUser(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        sex=data['sex'],
        contact_number=data['contact_number'],
        email_id=data['email_id'],
        password=data['password'],
        designation=data['designation']
    )
    db.session.add(new_user)
    db.session.commit()
    return {'success': True, 'message': 'Store user created successfully'}

def authenticate_store_user(email_id, password):
    user = StoreUser.query.filter_by(email_id=email_id).first()
    if user and check_password_hash(user.password, password):
        return {'success': True, 'message': 'Authentication successful', 'role': user.designation}
    return {'success': False, 'message': 'Invalid credentials'}
