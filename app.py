from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder=".")

users = {}


@app.get("/")
def home():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        users[email] = {"name": name, "password": password}
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = users.get(email)

        if user and user["password"] == password:
            return redirect(url_for("dashboard"))

        return "Invalid email or password", 401

    return render_template("login.html")


@app.get("/dashboard")
def dashboard():
    return render_template("user.html")


if __name__ == "__main__":
    app.run(debug=True)