'''
In Terminal :

==============================================================================================================
To run Flask App :-

export FLASK_APP=project
export debug=True
flask run --host=0.0.0.0 ( for all the machine connected with the same network)

==============================================================================================================

To Create db :-

from project.__init__ import create_app
from project.models import User,Room,Dates,Booking
app= create_app()

===============================================================================================================
'''

from flask import Flask
import flask_sqlalchemy
db = flask_sqlalchemy.SQLAlchemy()



def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///HotelCalifornia.db"
    app.config['SECURITY_PASSWORD_SALT'] = 'fhasdgihwntlgy8f'
    app.config["SESSION_COOKIE_PATH"] = "/"
    app.config["DEBUG"] = True

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .user import user_blueprint
    app.register_blueprint(user_blueprint)

    from .welcome import welcome_blueprint
    app.register_blueprint(welcome_blueprint)

    return app

    