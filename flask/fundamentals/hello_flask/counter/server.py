from flask import Flask, render_template, request, redirect ,session# added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/count', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['counter'] = request.form['counter']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')

@app.route("/form_click", methods = ["POST"])
def form_click():
    if 'counter' in session:
        print('key exists!')
        session['counter'] += 1
    else:
        print("key 'key_name' does NOT exist")
        session['counter'] = 1

    return render_template("index.html", counter=session['counter'])

@app.route("/form_refresh", methods = ["POST"])
def form_refresh():
    if 'counter' in session:
        print('key exists!')
        session['counter'] = 1
        return render_template("index.html", counter=session['counter'])
    else:
        print("key 'key_name' does NOT exist")

@app.route("/destroy_session", methods = ["GET"])
def destroy_session():
    if 'counter' in session:
        session.clear()
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
