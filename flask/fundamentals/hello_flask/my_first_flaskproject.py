from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    print(type(name))
    if(name.isnumeric()):
        return "Please type string/character"
    else:
        return "Hi " + name +"!"


@app.route('/repeat/<id>/<username>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(id, username):
    print(username)
    print(id)
    if(id.isnumeric()):
        num=int(id)
        newstr=""
        for i in range(0,num):
            newstr += "<div>" + username + "</div>"
            print(newstr)
        return newstr
    else:
        return "Please type integer in 2nd place"



# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
