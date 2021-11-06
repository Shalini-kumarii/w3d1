from flask import render_template, request, redirect ,session # added request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route("/create", methods = ["POST"])
def form_process():
    if not Dojo.validate_dojo(request.form):
        return redirect("/")
    id = Dojo.survey_create(request.form)
    return redirect(f'/show/{id}')


@app.route("/show/<id>")
def form_show(id):
    dojoinfo = Dojo.get_suvery({"id":id})
    print(dojoinfo)
    return render_template("result.html", dojoinfo=dojoinfo)

@app.route("/index")
def form_index():
    return render_template("index.html")