from flask import render_template, request, redirect ,session # added request
from flask_app import app
from flask_app.models.dojo import Dojo


# our index route will handle rendering our form

@app.route('/')
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos = dojos)

@app.route('/dojos/new')
def dojos():
    return render_template("index.html")

@app.route('/dojos/create',methods=["POST"])
def create_friend():
    print(request.form)
    Dojo.create(request.form)

    return redirect("/")

#  USE upper or lower
#  data = {
#         "fname": request.form["fname"],
#         "lname" : request.form["lname"],
#         "occ" : request.form["occ"]
#     }
#     # We pass the data dictionary into the save method from the Friend class.
#     Friend.save(data)
#     return redirect("/")

@app.route('/dojos/show/<id>')
def show_user(id):
    dojoinfo = Dojo.get_one({"id": id})
    return render_template("show.html", dojo = dojoinfo)

@app.route('/dojos/edit/<id>')
def edit_user(id):
    dojoinfo = Dojo.get_one({"id": id})
    return render_template("edit.html", dojo = dojoinfo)

@app.route('/dojos/update/<id>',methods=["POST"])
def do_update(id):
    data = {
        **request.form, # copies over all the data from the request.form dictionary
        "id": id
    }
    Dojo.update(data)
    return redirect(f"/dojos/show/{id}")

@app.route('/dojos/delete/<id>')
def do_delete(id):
    Dojo.delete({"id": id})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
