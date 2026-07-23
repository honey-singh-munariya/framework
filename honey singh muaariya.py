from flask import Flask, render_template

web = Flask(__name__, template_folder="template", static_folder="static")


@web.route("/", methods=["GET"])
def home():
    return render_template("regstration.html")


@web.route("/register", methods=["GET", "POST"], endpoint="register")
def register():
    return render_template("regstration.html")


if __name__ == "__main__":
    web.run(debug=True)
    