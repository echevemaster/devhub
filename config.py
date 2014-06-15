# -*- coding: utf-8 -*-
import os
# Belonging to the path of  sqlite development database.
basedir = os.path.abspath(os.path.dirname(__file__))
engine = ''  # sqlite, Mysql, postgres and so on.
db_name = ''
db_user = ''
db_password = ''
db_server = 'localhost'  # Usually, localhost


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}/{4}'.format(engine,
                                                             db_user,
                                                             db_password,
                                                             db_server,
                                                             db_name)
    DATABASE_CONNECT_OPTIONS = {}
    SECRET_KEY = 'key'
    CSRF_SESSION_KEY = "somethingimpossibletoguess"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = engine + ':///' + os.path.join(basedir,
                                                             db_name)
    DATABASE_CONNECT_OPTIONS = {}
    sQLALCHEMY_ECHO = True
    SECRET_KEY = 'This string will be replaced with a proper key in production'
    CSRF_SESSION_KEY = "somethingimpossibletoguess"


class TestingConfig(Config):
    TESTING = True
