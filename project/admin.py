from flask import Blueprint , current_app, request, session, redirect, url_for, render_template, flash
from .models import Room, User,Booking,Dates
from .__init__ import db
from datetime import datetime
from functools import wraps

admin_blueprint = Blueprint("admin_blueprint",__name__)

def checkAdmin(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        login_user_email= session["login_user_email"]
        if login_user_email == "murari@hulchul.com":
            User.query.filter_by(email=login_user_email).update({"admin":False})
            db.session.commit()
        isAdmin = (User.query.filter_by(email=login_user_email).first()).admin
        if not isAdmin:
            flash("You are not a admin")
            return redirect(url_for("welcome_blueprint.get_this_room"))
        return f(*args,**kwargs)
    return wrapper


@admin_blueprint.route("/admin", methods=["POST","GET"])
@checkAdmin
def admin():
    return render_template("admin.html")
