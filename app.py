# Importing the modules and framework

from flask import Flask, render_template, request

# inteacting 

web = Flask(__name__)

# mapping

@web.route('/')
@web.route('/register')

# Inputs
def homepage():
    return render_template("register.html")

# mapping the web
@web.route('/confirm', methods = ['POST','GET'])

# Taking the inputs

def confirm():
    if request.method == "POST":
        n = request.form.get("name")
        c = request.form.get("city")
        p = request.form.get("Phone_number")

        return render_template("confirm.html", name = n, city = c, phone_number = p)


# Main
if __name__ == "__main__":
    web.run(debug=True)

