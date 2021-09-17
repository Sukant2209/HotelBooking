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
            User.query.filter_by(email=login_user_email).update({"admin":True})
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

    if request.method=="POST":
        room_id = request.form.get('roomId')
        room_type = request.form.get("optradio")

        if room_type == "Single":
            room = Room(room_id=room_id,room_type="Single",room_price=800)
        elif room_type == "Double":
            room = Room(room_id=room_id,room_type="Double",room_price=1500)
        else:
            room = Room(room_id=room_id,room_type="Delux",room_price=3500)

        db.session.add(room)
        db.session.commit()

        flash("New Room created")

    return render_template("admin.html")




