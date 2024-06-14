# app/models/database.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# run.py (or main application file)
from flask import Flask
from config import Config
# from app.models.database import db, migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
