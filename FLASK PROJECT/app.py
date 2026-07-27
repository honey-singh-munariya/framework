# Importing the modules
from flask import Flask, render_template, request

web = Flask(__name__)


@web.route('/')
@web.route("/confirm")

def homepage():
    return render_template("form.html")

@web.route("/confirm", methods = ['POST', 'GET'])

def confirm():
    if request.method == "POST":
        n = request.form.get("name")
        e = request.form.get("email")
        p= request.form.get("phonenumber")
        c= request.form.get("city")

        return render_template("confirm.html",name=n, email=e, phonenumber=p,city=c)

    

if __name__ == "__main__":
    web.run(debug=True)


