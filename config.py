import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost:5432/replacements'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
