#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager
from devhub.app import app

manager = Manager(app)


@manager.command
def run():
    """ Run application """
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    manager.run()
