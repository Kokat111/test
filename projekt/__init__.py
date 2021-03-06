from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A5CF8ZH73XOSXG4PH9BD'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from projekt import routs
