from flask import Flask, render_template, request, redirect ,session # added request
from user import User
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route('/users/new')
def users():
    return render_template("users.html")

@app.route('/users/create',methods=["POST"])
def create_friend():
    print(request.form)
    User.create(request.form)

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

@app.route('/users/show/<id>')
def show_user(id):
    userinfo = User.get_one({"id": id})
    return render_template("show.html", userx = userinfo)

@app.route('/users/edit/<id>')
def edit_user(id):
    userinfo = User.get_one({"id": id})
    return render_template("edit.html", user = userinfo)

@app.route('/users/update/<id>',methods=["POST"])
def do_update(id):
    data = {
        **request.form, # copies over all the data from the request.form dictionary
        "id": id
    }
    User.update(data)
    return redirect(f"/users/show/{id}")

@app.route('/users/delete/<id>')
def do_delete(id):
    User.delete({"id": id})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
