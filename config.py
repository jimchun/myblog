import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Zoe%409820@localhost/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False