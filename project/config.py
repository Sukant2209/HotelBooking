class Config(object):
   SECRET_KEY = "secretkey"
   SQLALCHEMY_DATABASE_URI ="sqlite:///HotelCalifornia.db"
   SECURITY_PASSWORD_SALT = 'fhasdgihwntlgy8f'
   SESSION_COOKIE_PATH ="/"
   SESSION_PERMANENT=False
   DEBUG = True
   MAIL_SERVER='smtp.gmail.com'
   MAIL_PORT = 465
   MAIL_USERNAME = 'HotelCalifornia.india@gmail.com'
   MAIL_PASSWORD = 'Hotel@1992'
   MAIL_USE_TLS = False
   MAIL_USE_SSL = True