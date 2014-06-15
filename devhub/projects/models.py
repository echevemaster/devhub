# -*- coding: utf-8 -*-
"""
devhub.projects.models
~~~~~~~~~~~~~~~~~~~~~

Projects models
"""

from devhub.app import db


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text())
    homepage = db.Column(db.String(255))
