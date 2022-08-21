from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from portfolio import config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# Adding secret key to app configuration
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

# Creating database
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from portfolio import routes