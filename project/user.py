from flask import Blueprint , render_template , request , redirect, url_for
from flask_bcrypt import generate_password_hash , check_password_hash
from flask import current_app

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
            current_app.logger.info("Password do not match while Registering")
            return redirect(url_for("user_blueprint.index"))

        
        
        return redirect(url_for("user_blueprint.login"))


    return render_template("register.html")


@user_blueprint.route("/login")
def login():
    return render_template("login.html")