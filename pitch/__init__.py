
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '8842f7517ecf0393104bb6c30a420f74'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager  = LoginManager(app)

from pitch import views