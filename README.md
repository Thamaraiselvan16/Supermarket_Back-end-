# Supermarket Backend Application

## Installation Procedure

1. **Download or Clone the Repository**
    ```bash
    git clone https://github.com/Thamaraiselvan16/Supermarket_Back-end.git
    cd Supermarket_Back-end
    ```

2. **Extract the Downloaded File**
    ```bash
    unzip Supermarket_Back-end.zip
    ```

3. **Open Command Prompt (cmd)**

4. **Navigate to the Correct Directory**
    ```bash
    cd Supermarket_Back-end
    ```

5. **Install Virtualenv**
    ```bash
    pip install virtualenv
    ```

6. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

7. **Activate the Virtual Environment**
    ```bash
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

8. **Install the Requirements**
    ```bash
    pip install -r requirements.txt
    ```

9. **Change to the App Directory**
    ```bash
    cd app
    ```

10. **Set the FLASK_APP Environment Variable**
    ```bash
    setx SECRET_KEY "my_secret_key"
    setx DATABASE_URL "mysql+pymysql://user:password@localhost/supermarket_db" #need to change
    setx EMAIL "your_mail@gmail.com"
    setx EMAIL_PASSWORD "my-email-password"
    setx MANAGER_EMAIL "manager_mail@gmail.com"


    set FLASK_APP=run.py  # On Windows
    export FLASK_APP=run.py  # On macOS/Linux
    ```

11. **Run the Flask Application**
    ```bash
    flask run
    ```

12. **Access the Application**
    Open your browser and navigate to `http://127.0.0.1:5000`

13. **Update Configuration**
    Go to `app/config.py` and update the following:
    ```python
    class Config:
        SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/supermarket_db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        EMAIL_SERVER = 'smtp.gmail.com'
        EMAIL_PORT = 587
        EMAIL = os.getenv('EMAIL', 'your_mail@gmail.com')
        EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'your_email_password')
        MANAGER_EMAIL = os.getenv('MANAGER_EMAIL', 'manager_mail@gmail.com')
    ```

14. **Create Database**
```python
CREATE DATABASE supermarket_db;

USE supermarket_db;

CREATE TABLE User_details (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    sex ENUM('Male', 'Female', 'Other'),
    contact_number VARCHAR(15),
    email_id VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE Store_user (
    store_user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    sex ENUM('Male', 'Female', 'Other'),
    contact_number VARCHAR(15),
    email_id VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    designation ENUM('Manager', 'Sales Man')
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    rate DECIMAL(10, 2),
    stock INT
);

CREATE TABLE Purchase (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    email_id VARCHAR(100),
    item VARCHAR(100),
    quantity INT,
    rate DECIMAL(10, 2),
    date_of_purchase DATE,
    FOREIGN KEY (user_id) REFERENCES User_details(user_id),
    FOREIGN KEY (email_id) REFERENCES User_details(email_id)
);

SELECT * FROM User_details;
SELECT * FROM Store_user;
SELECT * FROM Products;
SELECT * FROM Purchase;
 ```