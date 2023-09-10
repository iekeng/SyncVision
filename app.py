#!/usr/bin/python3
"""main website flask app"""
from flask import Flask
from views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)