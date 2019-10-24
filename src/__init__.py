from flask import Flask
app = Flask(__name__)
import os

# database
from flask_sqlalchemy import SQLAlchemy

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)


#views
from src import views
from src.developers import views

#models

# create tables
try: 
    db.create_all()
except:
    pass