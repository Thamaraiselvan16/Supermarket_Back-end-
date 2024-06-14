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
