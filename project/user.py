import bcrypt
from flask import Blueprint , render_template , request , redirect, url_for , flash, session
from flask_bcrypt import generate_password_hash , check_password_hash
from flask import current_app
from .__init__ import db
from .models import User

user_blueprint = Blueprint("user_blueprint",__name__)


@user_blueprint.route("/", methods=["POST","GET"])
def index():
    if request.method=="POST":

        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        password = generate_password_hash(request.form.get("password"))
        password_confirmation = (request.form.get("passwordConfirmation"))
        

        if not check_password_hash(password, password_confirmation):
            flash("Password do not Match.. Please re-enter")
            current_app.logger.info("Password do not match while Registering")
            return redirect(url_for("user_blueprint.index"))

        registered_user_email = User.query.filter_by(email=email).first()
        if registered_user_email:
            print(registered_user_email.email)
            flash("You are already registered , Go To Login page")
            current_app.logger.info("You are already registered , Go To Login page")
            return redirect(url_for("user_blueprint.index"))

        user = User(first_name=firstname, last_name=lastname,email=email,password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("user_blueprint.login"))


    return render_template("register.html")


@user_blueprint.route("/login", methods=["POST","GET"])
def login():

    if request.method=="POST":
        email = request.form.get("email")
        password = request.form.get("password")

        login_user = User.query.filter_by(email=email).first()

        if not login_user:
            flash("Dont have a account yet ? Register Now")
            return redirect(url_for("user_blueprint.login"))

        if login_user.email == email and check_password_hash(login_user.password, password):
            session["login_user_email"] = login_user.email
            return redirect(url_for("welcome_blueprint.get_this_room"))


    return render_template("login.html")