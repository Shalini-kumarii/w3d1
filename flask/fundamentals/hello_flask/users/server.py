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

if __name__ == "__main__":
    app.run(debug=True)
