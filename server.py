from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_data = request.json
        username = login_data["username"]
        password = login_data["password"]
        # Tu wpisz kod logiki logowania
        if username == "admin" and password == "admin123":
            return {"message": "Success"}
        else:
            return {"message": "Failure"}
    else:
        return {"test": "test"}

if __name__ == "__main__":
    app.run(debug=True)
