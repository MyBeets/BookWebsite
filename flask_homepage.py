#!/usr/bin/env python

import flask
from flask import request, redirect

#http://127.0.0.1:5000/ 


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


@APP.route('/account/')
def account():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('account.html')

@APP.route('/add/')
def add():
    """ Displays the index page accessible at '/'
    """

    return flask.render_template('add.html')

@APP.route('/search/')
def search():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('not-implemented.html')

@APP.route('/add/signup/', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/add/')


if __name__ == '__main__':
    APP.debug=True
    APP.run()