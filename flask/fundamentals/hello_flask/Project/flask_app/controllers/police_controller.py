from flask import render_template, request, redirect ,session # added request
from flask_bcrypt import Bcrypt  
from flask_app import app
from flask_app.models.user import User
from flask_app.models.police import Police
      
bcrypt = Bcrypt(app) 
# police registration/Login -----------------

@app.route('/police_signup')
def police_signup():
    return render_template("police_login.html")

@app.route("/police_register", methods = ["POST"])
def police_register():
    if not Police.validate_register(request.form):
        return redirect("/police_signup")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        **request.form,
        "password" : pw_hash
    }

    police_id=Police.create(data)
    session["uuid"] = police_id      # unique user id
    return redirect("/police_signup")

    
@app.route("/police_login" , methods=["POST"])
def police_login():
    if not Police.login_validator(request.form):
        return redirect("/police_signup")
    police = Police.get_login_by_email({ "email":request.form["email"]})
    session["uuid"] = police.id
    return redirect("/police_dashboard")
