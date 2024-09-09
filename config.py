import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:yourpassword@localhost/flask_blog' #替换你的密码yourpassword
    SQLALCHEMY_TRACK_MODIFICATIONS = False
