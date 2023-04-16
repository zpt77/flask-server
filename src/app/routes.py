from app import app, db, start_time
from flask import jsonify, make_response, request
from app.models import Users
from werkzeug.security import generate_password_hash, check_password_hash


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
    if user and user.check_password(password):
        return jsonify({"message": "Success"}), 200
    else:
        return jsonify({"message": "Failure"}), 401
    

@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.json
    username = user_data["username"]
    password = user_data["password"]
    password_hash = generate_password_hash(password)

    user = Users(username=username, password_hash=password_hash)
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
            "password_hash": user.password_hash
        }
        users_list.append(user_dict)
    return jsonify({"users": users_list})
