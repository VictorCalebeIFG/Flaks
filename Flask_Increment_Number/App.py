from flask import Flask, render_template, flash, request

app = Flask(__name__)

number = 0
@app.route('/', methods = ["POST","GET"])

def index():
    global number
    if request.method == "POST":
        number += 1
    return render_template("index.html", number = str(number))