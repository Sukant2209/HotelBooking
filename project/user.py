from flask import Blueprint , render_template

user_blueprint = Blueprint("user_blueprint",__name__)


@user_blueprint.route("/")
def index():
    return render_template("register.html")


@user_blueprint.route("/login")
def login():
    return render_template("login.html")