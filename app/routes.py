from flask import Flask


app = Flask(__name__)



@app.route("/")
def index():
    return "<h1>Hello, world!</h1>"


@app.get("/home")
def home():
    return "Welcome home!"


@app.route("/about")
def about_me():
    me = {
        "first_name": "Miguel",
        "last_name": "Renteria",
        "hobbies": "Crossfit",
        "active": True,
        "lists": [1,2,3],

    }    
    return me 


