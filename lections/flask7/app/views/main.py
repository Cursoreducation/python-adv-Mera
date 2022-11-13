from flask import render_template, Blueprint


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    return render_template("index.html")

@main_blueprint.route("/about")
def about():
    return render_template("about.html")


