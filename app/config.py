import os
class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True
    PORT = 3004
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False