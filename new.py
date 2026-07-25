# importing the module and framework
from flask import Flask, render_template

# INTERACTION

app = Flask(__name__)

# Mapping the web

@app.route("/")

def first():
    return render_template("home.html")

# input

@app.route("/second")

def home():
    return "Welcome to the second page"

# main
if __name__ == "__main__":
    app.run(debug=True)