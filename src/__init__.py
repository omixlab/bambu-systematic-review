import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table, create_engine

import src
from src.celery_utils import make_celery

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
celery = make_celery(app)
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Please login"
login_manager.login_category = "info"
from src import routes
