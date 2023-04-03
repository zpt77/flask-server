from flask import Flask, request, jsonify

app = Flask(__name__)

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
