from flask import Blueprint
from flask.templating import render_template


welcome_blueprint = Blueprint("welcome_blueprint",__name__)

@welcome_blueprint.route("/profile")
def welcomePage():
    return render_template("profile.html")
