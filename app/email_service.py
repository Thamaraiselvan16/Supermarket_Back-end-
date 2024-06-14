# app/email_service.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models.purchase import Purchase
from datetime import datetime, timedelta
from flask import current_app as app
from run import create_app 

def send_email(subject, body, to_email):
    app = create_app()
    with app.app_context():
        from_email = app.config['EMAIL']
        password = app.config['EMAIL_PASSWORD']
        email_server = app.config['EMAIL_SERVER']
        email_port = app.config['EMAIL_PORT']

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(email_server, email_port)
            server.starttls()
            server.login(from_email, password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
            return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

def generate_sales_report(start_date, end_date):
    app = create_app()
    with app.app_context():
        sales_data = Purchase.query.filter(Purchase.date_of_purchase.between(start_date, end_date)).all()
        report = {}
        for sale in sales_data:
            item = sale.item
            if item not in report:
                report[item] = {'QTY': 0, 'Amount': 0}
            report[item]['QTY'] += sale.quantity
            report[item]['Amount'] += sale.quantity * float(sale.rate)
        return report

def send_daily_sales_report():
    app = create_app()
    with app.app_context():
        end_date = datetime.today().date()
        start_date = end_date - timedelta(days=1)
        report = generate_sales_report(start_date, end_date)
        body = str(report)
        send_email("Daily Sales Report", body, app.config['MANAGER_EMAIL'])

def send_weekly_sales_report():
    app = create_app()
    with app.app_context():
        end_date = datetime.today().date()
        start_date = end_date - timedelta(days=end_date.weekday() + 1)  # Last Monday
        report = generate_sales_report(start_date, end_date)
        body = str(report)
        send_email("Weekly Sales Report", body, app.config['MANAGER_EMAIL'])
