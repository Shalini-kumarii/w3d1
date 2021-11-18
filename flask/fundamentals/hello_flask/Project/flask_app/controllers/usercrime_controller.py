from flask import render_template, request, redirect ,session # added request

from flask_app import app
from flask_bcrypt import Bcrypt   
from flask_app.models.crimes import Crimes
from flask_app.models.user import User
bcrypt = Bcrypt(app) 

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", 
    logged_in_user = User.get_login_by_id({"id": session["uuid"]}),
    all_crime=Crimes.get_crime_data_with_userid({"user_id": session["uuid"]})
    )

@app.route("/users/new")
def new_crime():
    print(session["uuid"])
    return render_template("create.html",
    logged_in_user = User.get_login_by_id({"id": session["uuid"]}))

@app.route("/users/create",methods = ["POST"])
def create_crime():
    if not Crimes.validate(request.form):
        return redirect("/users/new")
    print("here1")
    data={
        **request.form,
        "user_id":session["uuid"]
    }
    print(data)
    Crimes.create(data)
    print("here2")
    return redirect("/dashboard")

@app.route("/users/<int:id>")
def display_usercrime(id):
    return render_template(
        "show_instructions.html",
        logged_in_user = User.get_login_by_id({"id": session["uuid"]}),
        crime=Crimes.get_one({"id": id})
    )
@app.route("/users/<int:id>/edit")
def edit_crime(id):
    crimelist=['Stone pelting on freeway','Package theft','Road rage','Abuse']
    neighborhood_list=['Bear Creek','Grass Lawn','Education Hill']
    return render_template(
        "edit.html",
        crime=Crimes.get_one({"id": id}),
        crimelist=crimelist,
        neighborhood_list=neighborhood_list)
    
@app.route("/users/<int:id>/update",methods = ["POST"])
def update_crime(id):
    if not Crimes.validate_update(request.form):
        return redirect(f"/users/{id}/edit")
    data={  
        **request.form,
        "id": id
    }
    Crimes.update(data)
    print(data)
    return redirect("/dashboard")

@app.route("/users/<int:id>/delete")
def delete_crime(id):
    Crimes.delete({"id": id})
    
    return redirect("/dashboard")