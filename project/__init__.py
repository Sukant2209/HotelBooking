'''
In Terminal :

==============================================================================================================
To run Flask App :-

export FLASK_APP=project
export debug=True
flask run --host=0.0.0.0 ( for all the machine connected with the same network)

==============================================================================================================
To Activate virtual Env:-

source venv/bin/activate

To Create virtual Env:-

python3 -m venv /path/to/new/virtual/environment
==============================================================================================================

To Create db :-

from project.__init__ import create_app
from project.models import User,Room,Dates,Booking
app= create_app()

===============================================================================================================
'''

from flask import Flask
import flask_sqlalchemy
from flask_mail import Mail
from .config import Config

db = flask_sqlalchemy.SQLAlchemy()
mail=Mail()



def create_app():

    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    from .user import user_blueprint
    app.register_blueprint(user_blueprint)

    from .welcome import welcome_blueprint
    app.register_blueprint(welcome_blueprint)

    from .admin import admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app

    