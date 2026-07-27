# Importing the modules and framework

from flask import Flask, render_template, request
import os
# inteacting 
web = Flask(__name__)


pic_folder = os.path.join('static')
web.config['UPLOAD_FOLDER'] = pic_folder

# mapping

@web.route('/')
@web.route('/register')

# Inputs
def homepage():
    pic = os.path.join(web.config['UPLOAD_FOLDER'],'s8hIt7qZOPR1gKtZzfAneEEr8pb.webp')
    return render_template("register.html",user_image = pic)

# mapping the web
@web.route('/confirm', methods = ['POST','GET'])

# Taking the inputs

def confirm():
    if request.methods == "POST":
        n = request.form.get("name")
        c = request.form.get("city")
        p = request.form.get("Phone_number")

        return render_template("confirm.html", name = n, city = c, phone_number = p)
    
# Main
if __name__ == "__main__":
    web.run(debug=True)

