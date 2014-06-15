# -*- coding: utf-8 -*-
"""
devhub.users.models
~~~~~~~~~~~~~~~~~~~~~

User models
"""

from devhub.app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    firstname = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    password = db.Column(db.String(120))
    homepage = db.Column(db.String(255))
    bio = db.Column(db.Text())
    rss_url = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime())
    date_registered = db.Column(db.DateTime())
    active = db.Column(db.Boolean())

    def __repr__(self):
        return '<Username %r' % (self.username)
