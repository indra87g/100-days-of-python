"""
Day 16 - Flask Auth

Getting Started:
* Install flask by running 'pip install flask'
* Run the webserver by running 'flask run --debug'
* Open 'localhost:5000' on web browser
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3 as sq

app = Flask(__name__)
app.secret_key = "hello_world"
app.config["DATABASE"] = "database/auth.sqlite"


def connect_db():
    conn = sq.connect(app.config["DATABASE"])
    conn.row_factory = sq.Row
    return conn


@app.route("/")
def index():
    if "user_id" in session:
        return "Logged in as " + session["username"]
    return "You are not logged in!"


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)

        conn = connect_db()
        try:
            conn.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, hashed_password),
            )
            conn.commit()
        except sq.IntegrityError:
            flash("Username already taken!")
            return redirect(url_for("register"))
        finally:
            conn.close()
        flash("Registration successful, please login")
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = connect_db()
        user = conn.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if user is None:
            flash("Incorrect username")
            return redirect(url_for("login"))

        if not check_password_hash(user["password"], password):
            flash("Incorrect password")
            return redirect(url_for("login"))

        session["user_id"] = user["id"]
        session["username"] = user["username"]
        return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    flash("You logged out.")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
