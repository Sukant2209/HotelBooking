'''
In Terminal :
export FLASK-APP=project
export debug=True
flask run --host=0.0.0.0 ( for all the machine connected with the same network)
'''

from flask import Flask
import flask_sqlalchemy


db = flask_sqlalchemy.SQLAlchemy()



def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///HotelCalifornia.db"

    db.init_app(app)

    db.create_all()

    from .user import user_blueprint
    app.register_blueprint(user_blueprint)

    return app