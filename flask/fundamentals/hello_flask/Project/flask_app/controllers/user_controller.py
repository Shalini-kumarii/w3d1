from flask import render_template, request, redirect ,session # added request
from flask_bcrypt import Bcrypt  
from flask_app import app
from flask_app.models.user import User
from flask_app.models.police import Police
      
bcrypt = Bcrypt(app) 


@app.route('/')
def index():
    return render_template("index.html")

# user registration/Login -----------------

@app.route('/user_signup')
def user_signup():
    return render_template("user_login.html")

@app.route("/register", methods = ["POST"])
def register():
    if not User.validate_register(request.form):
        return redirect("/user_signup")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        **request.form,
        "password" : pw_hash
    }

    user_id=User.create(data)
    session["uuid"] = user_id      # unique user id
    return redirect("/user_signup")

    
@app.route("/login" , methods=["POST"])
def login():
    if not User.login_validator(request.form):
        return redirect("/user_signup")
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