from flask import Flask, render_template

web = Flask(__name__)

@web.route("/")

def inheraten():
    return render_template("base.html")

if __name__ == "__main__":
    web.run(debug=True)