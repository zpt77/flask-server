from flask_sqlalchemy import SQLAlchemy
from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(256))

    def __init__(self, username, password):
        self.username = username
        self.password = password