import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from tracker.config import Config


template_dir = os.path.abspath('tracker/templates')
app = Flask(__name__, template_folder=template_dir)
app.config.from_object(Config)
db = SQLAlchemy(app)
