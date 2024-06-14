# config.py

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:thamarai5118@localhost/supermarket_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    EMAIL_SERVER = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL = os.getenv('EMAIL', 'dhill7228@gmail.com')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'pvgx jamx fvgt orpj')
    MANAGER_EMAIL = os.getenv('MANAGER_EMAIL', 'tthamaraiselvan2002@gmail.com')
