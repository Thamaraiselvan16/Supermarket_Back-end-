# run.py
from flask import Flask
from routes.user_routes import user_bp
from routes.product_routes import product_bp
from routes.store_user_routes import store_user_bp
from routes.purchase_routes import purchase_bp
from models.database import db, migrate
from config import Config
from apscheduler.schedulers.background import BackgroundScheduler


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(purchase_bp, url_prefix='/api')
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(store_user_bp, url_prefix='/api')


    with app.app_context():
        db.create_all()
        
        # Scheduler setup
        from email_service import send_daily_sales_report, send_weekly_sales_report
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=send_daily_sales_report, trigger='cron', hour=22, minute=0, second=0)
        scheduler.add_job(func=send_weekly_sales_report, trigger='cron', day_of_week='sat', hour=11, minute=0, second=0)
        scheduler.start()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
