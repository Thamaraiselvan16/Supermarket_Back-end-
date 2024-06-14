# config.py

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/database_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
    EMAIL_SERVER = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL = os.getenv('EMAIL', 'your_mail@gmail.com')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'llll bbbb cccc nnnn')
    MANAGER_EMAIL = os.getenv('MANAGER_EMAIL', 'manager_mail@gmail.com')
