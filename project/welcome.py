from flask import Blueprint , current_app, request, session, redirect, url_for, render_template, flash
from flask_mail import Message
from .models import Room, User,Booking,Dates
from .__init__ import db , mail
from datetime import datetime
import random


welcome_blueprint = Blueprint("welcome_blueprint",__name__)


def CREATE_ROOM():

    room1 = Room(room_id=101,room_type="Single",room_price=800)
    room2 = Room(room_id=201,room_type="Single",room_price=800)
    room3 = Room(room_id=301,room_type="Single",room_price=800)
    room4 = Room(room_id=401,room_type="Single",room_price=800)
    room5 = Room(room_id=501,room_type="Double",room_price=1500)
    room6 = Room(room_id=601,room_type="Double",room_price=1500)
    room7 = Room(room_id=701,room_type="Double",room_price=1500)
    room8 = Room(room_id=801,room_type="Double",room_price=1500)
    room9 = Room(room_id=901,room_type="Delux",room_price=3500)
    room10 = Room(room_id=1001,room_type="Delux",room_price=3500)

    total_rooms = [room1,room2,room3,room4,room5,room6,room7,room8,room9,room10]
    return total_rooms

def UNIQUE_BOOKING_ID():
    sequence1=['elgnis','elboud','xuled','detaerc','atad','moor','epyt','tnirp']
    sequence2=['aidni','acirema','rupiaj']
    sequence3=[x for x in range(2,100)]
    sequence4=['a','e','i','o','u']

    booking_id= f'hc{random.choice(sequence1)}{random.choice(sequence2)}{random.choice(sequence3)}{random.choice(sequence4)}'

    return booking_id


def SEND_MAIL(login_user_email):
    msg = Message(subject="Your booking @HotelCalifornia",
                  body="You are booked",
                  sender="hotelcalifornia.india@gmail.com",
                  recipients=[login_user_email]
                 )
    mail.connect()
    mail.send(msg)
    return "Success"



@welcome_blueprint.route("/allroomDetails")
def room_details():

    # total_rooms = CREATE_ROOM()

    # for x in total_rooms:
    #     db.session.add(x)
    #     db.session.commit()

    room_fetch_from_db = Room.query.all()
    print(room_fetch_from_db)
    current_app.logger.info(room_fetch_from_db)
    return render_template("profile.html")


@welcome_blueprint.route("/getRoom")
def get_this_room():

    if not "login_user_email" in session:
        return redirect(url_for("user_blueprint.login"))
        

    get_room_from_profile = request.args.get('type')

    this_room = Room.query.filter_by(room_type=get_room_from_profile).all()

    return render_template("profile.html",this_room=this_room)


@welcome_blueprint.route("/confirmRoom", methods=["POST","GET"])
def confirm_this_room():

    if not "login_user_email" in session:
        return redirect(url_for("user_blueprint.login"))

    if request.method=="POST":
        selected_room_id = request.form.get("roomChecked")
        selected_room_id_details = Room.query.filter_by(room_id=selected_room_id).first()


        session["selected_room_id_details"] = selected_room_id_details

    return render_template("RoomConfirmation.html",selected_room_id_details = selected_room_id_details)


@welcome_blueprint.route("/roomBooked", methods=["POST","GET"])
def room_booked():

    print(session["selected_room_id_details"])
    print(session["login_user_email"])

    if "selected_room_id_details"  and "login_user_email" in session:

        selected_room_id_details = session["selected_room_id_details"]

        login_user_email = session["login_user_email"]
       

    booking_id = UNIQUE_BOOKING_ID()

    select_from_date = datetime.strptime(request.form.get("selectFrom"), '%Y-%m-%d')

    select_to_date = datetime.strptime(request.form.get("selectTo"), '%Y-%m-%d')

    if select_to_date <= select_from_date:
        flash("End date is before or equal to start date ! Please Select Again")
        return render_template("RoomConfirmation.html",selected_room_id_details = selected_room_id_details)


    booking = Booking(booking_id = booking_id,user_id=login_user_email,booked_room = selected_room_id_details["room_id"])
    db.session.add(booking)
    dates = Dates(date_from=select_from_date,date_to=select_to_date,user_id=login_user_email)
    db.session.add(dates)

    Room.query.filter_by(room_id=selected_room_id_details["room_id"]).update({"room_availability":False})
    db.session.commit()
    
    SEND_MAIL(login_user_email)

    return render_template("finalBookedPage.html")


@welcome_blueprint.route("/logout", methods=["POST","GET"])
def logout():
    session.clear()
    return redirect(url_for("user_blueprint.login"))