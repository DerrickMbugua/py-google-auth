from flask import Flask, session, abort, redirect, request, render_template

app = Flask(__name__)
app.secret_key = "mylongsecretkey"

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper

@app.route("/")
def hello_world():
    return render_template("index.html")
  
@app.route("/login")
def login():
    session["google_id"] = "Test"
    return redirect("/dashboard")
  
@app.route("/callback")
def callback():
    return "<p>Callback!</p>"
  
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
  
@app.route("/dashboard")
@login_is_required
def dashboard():
    return render_template("dashboard.html")