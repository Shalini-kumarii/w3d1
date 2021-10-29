from flask import Flask, render_template
import matplotlib
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("playground.html",phrase="first")	# notice the 2 new named arguments!


@app.route('/play/<number>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def play(number):
    print(number)
    if(number.isnumeric()):
        num=int(number)
        return render_template("playground.html",phrase="second",value=num)
    else:
        return "Please type integer in 2nd place"

@app.route('/play/<number>/<color>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def color(number,color):
    print(number)
    if(number.isnumeric()):
        num=int(number)
   
        return render_template("playground.html",phrase="third",value=num,colors=matplotlib.colors.cnames[color])
    else:
        return "Please type integer in 2nd place"


# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
