from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("checkboard.html",phrase="first")	# notice the 2 new named arguments!
@app.route('/<number>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def checkboard(number):
    print(number)
    if(number.isnumeric()):
        num=int(number)
        return render_template("checkboard.html",phrase="second",value=num)
    else:
        return "Please type integer in 2nd place"
@app.route('/<x>/<y>')
def checkboard2(x,y):
    
    if(x.isnumeric() and y.isnumeric()):
        numx=int(x)
        numy=int(y)
        return render_template("checkboard.html",phrase="third",row=numx,col=numy)
    else:
        return "Please type integer in 2nd place"
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
