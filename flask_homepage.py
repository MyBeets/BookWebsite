#!/usr/bin/env python

import flask
from flask import request, redirect

#mongo
from mongo_script import *

exec(open("mongo_script.py").read())

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
    return flask.render_template('search.html')


"""
ROUTES FOR FUNCTIONS
"""
@APP.route('/search/results/', methods = ['POST'])
def results():
    book_id = db_format(request.form['book_id'])
    search_results = db_search(book_id)
    return display_results(search_results)


@APP.route('/add/add_book/', methods = ['POST'])
def add_book():
    title = db_format(request.form['title'])
    author = db_format(request.form['author'])
    genres = db_format(request.form['genres']).split(",")
    print("The book is " + title + ", " + author)
    db_add_book(title, author, genres, [])
    return redirect('/add/')

@APP.route('/add/add_edge/', methods = ['POST'])
def add_edge():
    book1 = request.form['book1']
    book2 = request.form['book2']
    print("The edge is " + book1 + ", " + book2)
    db_add_edge(book1, book2)
    return redirect('/add/')

@APP.route('/book/', methods = ['POST'])
def book_main():
    book = request.form.to_dict()
    print("___" + str(book) + "___")
    print( type(book) )
    return flask.render_template('book.html', book = book)


"""
FUNCTIONS WITHOUT ROUTES
"""

def display_results(search_results):
    """ Displays the index page accessible at '/'
    """
    books = []
    #print("DEBUG")
    #print(search_results)
    for book in search_results:
            books.append(book)
            print(book)


    return flask.render_template('display_results.html', results = books)

def display_book_main(book):
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('book.html', book = book)


if __name__ == '__main__':
    APP.debug=True
    APP.run()