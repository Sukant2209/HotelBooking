from .__init__ import db
from datetime import datetime

class User(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    admin = db.Column(db.Boolean, nullable = False , default=False)
    dates = db.relationship("Dates", backref="Person", lazy = True)
    booking = db.relationship("Booking", backref="Person", lazy = True)

class Room(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    room_id = db.Column(db.Integer,nullable=False)
    room_availability = db.Column(db.Boolean,nullable=False)


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
