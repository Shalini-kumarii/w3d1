from flask import Flask, render_template, request, redirect ,session# added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def form_process():
    print(request.form)
    return render_template("result.html",fname=request.form["fname"],
    location=request.form["location"],
    languge=request.form["languge"],
    comment=request.form["comment"])

@app.route("/result", methods = ["POST"])
def form_refresh():

        return render_template("index.html")
   

if __name__ == "__main__":
    app.run(debug=True)
