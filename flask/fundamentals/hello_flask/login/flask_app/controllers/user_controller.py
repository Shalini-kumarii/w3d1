from flask import render_template, request, redirect ,session # added request
from flask_bcrypt import Bcrypt  
from flask_app import app
from flask_app.models.user import User
      
bcrypt = Bcrypt(app) 


@app.route('/')
def index():
    
    return render_template("index.html")

@app.route("/register", methods = ["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        **request.form,
        "password" : pw_hash
    }

    user_id=User.create(data)
    session["uuid"] = user_id      # unique user id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", user = User.get_login_by_id({"id": session["uuid"]}))

@app.route("/login" , methods=["POST"])
def login():
    if not User.login_validator(request.form):
        return redirect("/")
    user = User.get_login_by_email({ "email":request.form["email"]})
    session["uuid"] = user.id
    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/index")
def form_index():
    return render_template("index.html")