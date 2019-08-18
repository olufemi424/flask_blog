from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '061a9d20aa9aec2f897c7e0e115f65c0'
# connect to database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Authentication library
login_manager = LoginManager(app) #powerful login library
login_manager.login_view = 'login' # route function name
login_manager.login_message_category = 'info' #style alert message

# no format
from flaskblog import routes
