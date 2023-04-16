from flask import Flask, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
import sqlite3
from os import path

DB_NAME = "database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)

start_time = datetime.datetime.now().replace(microsecond=0)

class Users(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(30))
     password = db.Column(db.String(256))

     def __init__(self,username,password):
          self.username = username
          self.password = password

@app.route("/", methods=["GET"])
def home():
    html_content = f"<html><body><h1>Flask Server is running!</h1><p>Started at: {start_time}</p></body></html>"
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response

@app.route("/name", methods=["GET"])
def name_get():
    return jsonify({"server_name": "Flask"})

@app.route("/login", methods=["POST"])
def login():
    login_data = request.json
    username = login_data["username"]
    password = login_data["password"]
    user = Users.query.filter_by(username=username).first()

    if user is not None and user.password == password:
        return jsonify({"message": "Success"}), 200
    else:
        return jsonify({"message": "Failure"}), 401

@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.json
    username = user_data["username"]
    password = user_data["password"]
    user = Users(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 200

@app.route("/get_users", methods=["GET"])
def get_users():
    users = Users.query.all()
    users_list = []
    for user in users:
        user_dict = {
            "id": user.id,
            "username": user.username,
            "password": user.password
        }
        users_list.append(user_dict)
    return jsonify({"users": users_list})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
