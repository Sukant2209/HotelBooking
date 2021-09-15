from .__init__ import db
from datetime import datetime
from dataclasses import dataclass

class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    admin = db.Column(db.Boolean, nullable = False , default=False)
    dates = db.relationship("Dates", backref="Person_date", lazy = True)
    booking = db.relationship("Booking", backref="Person_book", lazy = True)

@dataclass
class Room(db.Model):
    id:int
    room_id:int
    room_availability:bool
    room_type:str
    room_price:int
    
    id = db.Column(db.Integer,primary_key=True)
    room_id = db.Column(db.Integer,nullable=False)
    room_availability = db.Column(db.Boolean,nullable=False, default=True)
    room_type = db.Column(db.String(30),nullable=False)
    room_price = db.Column(db.Integer,nullable=False)
    booking = db.relationship("Booking", backref="Room_book", lazy = True)


class Dates(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date_from = db.Column(db.DateTime, nullable=False)
    date_to = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"), nullable = False)


class Booking(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    booking_id = db.Column(db.String(40), nullable=False)
    booking_date = db.Column(db.DateTime, nullable=False , default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"), nullable = False)
    booked_room = db.Column(db.Integer,db.ForeignKey("room.room_id"), nullable = False)
