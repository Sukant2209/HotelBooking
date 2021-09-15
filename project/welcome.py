from flask import Blueprint , jsonify
from flask.templating import render_template
from .models import Room
from .__init__ import db

welcome_blueprint = Blueprint("welcome_blueprint",__name__)

@welcome_blueprint.route("/profile")
def welcomePage():
    return render_template("profile.html")



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


@welcome_blueprint.route("/allroomDetails")
def room_details():

    # total_rooms = CREATE_ROOM()

    # for x in total_rooms:
    #     db.session.add(x)
    #     db.session.commit()

    room_fetch_from_db = Room.query.all()

    return jsonify(room_fetch_from_db)