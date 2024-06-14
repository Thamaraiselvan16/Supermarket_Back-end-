Design and develop a backend application that maintains the stocks and
sales of a supermarket. The software must also record the individual
purchase history of each user.

INSTALLATION PROCEDURE: Github:
https://github.com/Thamaraiselvan16/Supermarket_Back-end- 1. Download or
clone the repository from GitHub. 2. Extract the downloaded file. 3.
Open the Command Prompt (cmd). 4. Navigate to the correct directory
where the files are extracted. 5. Install virtualenv using the command

pip install virtualenv

6\. Create a virtual environment using the command python -m venv
venv_file_name 7. Activate the virtual environment with the command:

pip install -r requirements.txt 8. Change to the app directory

cd app

9\. Set the FLASK_APP environment variable:

set FLASK_APP=run.py 10. Run the Flask application

flask run

11\. The application will start and be accessible at

http://127.0.0.1:5000

12\. Go to : app\\config.py  Need to Change class Config: SECRET_KEY =
os.getenv(\'SECRET_KEY\', \'default_secret_key\')
SQLALCHEMY_DATABASE_URI = os.getenv(\'DATABASE_URL\',
\'mysql+pymysql://user:password@localhost/your_database_name\')
SQLALCHEMY_TRACK_MODIFICATIONS = False

EMAIL_SERVER = \'smtp.gmail.com\' EMAIL_PORT = 587 EMAIL =
os.getenv(\'EMAIL\', \'your_mail@gmail.com\') EMAIL_PASSWORD =
os.getenv(\'EMAIL_PASSWORD\', \'gggg uuuu eeee llll\') MANAGER_EMAIL =
os.getenv(\'MANAGER_EMAIL\', \'manager_mail@gmail.com\')

FOLDER STRUCTURE: 1. Supermarket o App  Config.py  Email_service.py 
Run.py • Models o Database.py o Products.py o Purchase.py o
Store_user.py o User_details.py • Routes o Product_routes.py o
Purchase_routes.py o Store_user_routes.py o User_routes.py • Services o
Product_service.py o Purchase_service.py o Store_user_service.py o
User_service.py • Utils o Decorators.py

IN THIS STRUCTURE: 1. Routes handle incoming HTTP requests and map them
to the appropriate service methods. 2. Services contain the business
logic and interact with the Models. 3. Models define the data structures
and interact with the database.

CREATE DATABASE - MYSQL DATABASE: CREATE DATABASE supermarket_db; use
supermarket_db; CREATE TABLE User_details ( user_id INT AUTO_INCREMENT
PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), age INT, sex
ENUM(\'Male\', \'Female\', \'Other\'), contact_number VARCHAR(15),
email_id VARCHAR(100) UNIQUE, password VARCHAR(255) ); CREATE TABLE
Store_user ( store_user_id INT AUTO_INCREMENT PRIMARY KEY, first_name
VARCHAR(50), last_name VARCHAR(50), age INT, sex ENUM(\'Male\',
\'Female\', \'Other\'), contact_number VARCHAR(15), email_id
VARCHAR(100) UNIQUE, password VARCHAR(255), designation
ENUM(\'Manager\', \'Sales Man\') ); CREATE TABLE Products ( product_id
INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(100), rate
DECIMAL(10, 2), stock INT );

CREATE TABLE Purchase ( purchase_id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT, item VARCHAR(100), quantity INT, rate DECIMAL(10, 2),
date_of_purchase DATE, FOREIGN KEY (user_id) REFERENCES
User_details(user_id) ); CREATE TABLE Purchase ( purchase_id INT
AUTO_INCREMENT PRIMARY KEY, user_id INT, email_id VARCHAR(100), item
VARCHAR(100), quantity INT, rate DECIMAL(10, 2), date_of_purchase DATE,
FOREIGN KEY (user_id) REFERENCES User_details(user_id), FOREIGN KEY
(email_id) REFERENCES User_details(email_id) ); select \* from
User_details; select \* from Store_user; select \* from Products; select
\* from Purchase;

Develop a simple REST-API using python FLASK with the following
modules: 1. User Signup: (POST) http://127.0.0.1:5000/api/user/signup {
\"first_name\": \"your_first_name\", \"last_name\":
\"yore_second_name\", \"age\": 25, \"sex\": \"Male\",
\"contact_number\": \"9738264774\", \"email_id\":
\"your_mail@gmail.com\", \"password\": \"your_pass@123\" }

2\. User Login: (POST) http://127.0.0.1:5000/api/user/login {
\"email_id\": \"your_mail@gmail.com\", \"password\": \" your_pass@123\"
}

3\. Purchase: (POST) http://127.0.0.1:5000/api/purchase { \"email_id\":
\" your_mail gmail.com\", \"item\": \"apple\", \"quantity\": 20,
\"rate\": 150.00, \"date_of_purchase\": \"2024-06-12\" }

4\. Endpoints (GET) Date_filter:
http://127.0.0.1:5000/api/total_items?start_date=2024-06-10&end_date=2024-06-13
High_purchase: http://127.0.0.1:5000/api/high_purchases Shampoo_sales:
http://127.0.0.1:5000/api/shampoo_sales

5\. Add, Update, Delete a. Add (POST)
http://127.0.0.1:5000/api/shampoo_sales Postman / Headers key value
Content-Type application/json

Authorization Bearer \<your_jwt_token\>

b\. Update (PUT) http://127.0.0.1:5000/api/product/3 Postman / Headers
key value Content-Type application/json

Authorization Bearer \<your_jwt_token\>

c\. Delete (DELETE) http://127.0.0.1:5000/api/product/5 Postman /
Headers key value Content-Type application/json

Authorization Bearer \<your_jwt_token\>

6\. Store User Signup http://127.0.0.1:5000/api/store_user/signup {
\"first_name\": \"sundhar\", \"last_name\": \"A\", \"age\": 36, \"sex\":
\"Male\", \"contact_number\": \"776655443\", \"email_id\":
\"sundhar@gmail.com\", \"password\": \"sundhar@123\", \"designation\":
\"Manager\" }

7\. Store User login http://127.0.0.1:5000/api/store_user/login {
\"email_id\": \"sundhar@gmail.com\", \"password\": \"sundhar@123\" }

By, Thamaraiselvan
