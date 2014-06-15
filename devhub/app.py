# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Instantiate application.
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Instantiate database object
db = SQLAlchemy(app)

# Import application Blueprints.
