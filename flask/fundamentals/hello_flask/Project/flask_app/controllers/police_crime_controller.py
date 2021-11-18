from flask import render_template, request, redirect ,session # added request

from flask_app import app
from flask_bcrypt import Bcrypt   
from flask_app.models.crimes import Crimes
from flask_app.models.user import User
from flask_app.models.police import Police
bcrypt = Bcrypt(app) 

@app.route("/police_dashboard")
def police_dashboard():
    return render_template("police_search.html", 
    logged_in_police = Police.get_login_by_id({"id": session["uuid"]}))

@app.route("/police/search", methods=["POST"])
def display_crime():
    data = {
        **request.form
    }
    return render_template(
        "police_search.html",
        logged_in_police = Police.get_login_by_id({"id": session["uuid"]}),
        searched_crime=Crimes.get_crime_data(data)
    )


@app.route("/police/<int:id>/edit")
def edit_crimeStatus(id):
    crimelist=['Stone pelting on freeway','Package theft','Road rage','Abuse']
    neighborhood_list=['Bear Creek','Grass Lawn','Education Hill']
    status_list=['Open','Closed','Resolved']
    return render_template(
        "police_update.html",
        crime=Crimes.get_one({"id": id}),
        crimelist=crimelist,
        neighborhood_list=neighborhood_list,
        status_list=status_list)


@app.route("/police/<int:id>/update",methods = ["POST"])
def update_reportedCrime(id):
    # if not Police.validate_policeupdate(request.form):
    #     return redirect(f"/police/{id}/edit")
    data={  
        **request.form,
        "id": id
    }
    Police.update_Crime(data)
    print(data)
    return redirect("/police_dashboard")