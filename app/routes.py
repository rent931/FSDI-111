from flask import Flask


app = Flask(__name__)



@app.route("/")
def index():
    return "<h1>Hello, world!</h1>"


@app.get("/home")
def home():
    return "Welcome home!"


@app.route("/about", methods=["GET"])
def about():
    return "Hi, my name is Miguel Renteria."

