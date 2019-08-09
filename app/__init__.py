# This module defines the flask app
# and ties the different modules together

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

