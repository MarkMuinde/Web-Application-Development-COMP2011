import logging
from flask import render_template, flash, request, redirect, url_for, make_response
from app import app
from app import db
from .forms import BookForm
from app.models import BookList, Author


#home page
@app.route('/')
def booklist():
    form = BookForm()
    incomplete = BookList.query.filter_by(complete=False).all()
    complete = BookList.query.filter_by(complete=True).all()
    
    app.logger.info('BookList Launch successful')
    return render_template('book.html', title='Simple Booklist', incomplete=incomplete, 
                                        complete=complete, form=form)

#route for creating titles
@app.route('/createbook', methods=['GET', 'POST'])
def createBook():
    form = BookForm()
    incomplete = BookList.query.filter_by(complete=False).all()
    complete = BookList.query.filter_by(complete=True).all()
    t = BookList(booktitle=form.title.data, description=form.description.data,
                 startdate=form.date.data, complete=False)
    db.session.add(t)
    db.session.commit()
    app.logger.info('Book successfully added')
    return redirect(url_for('booklist'))

#route for completed books
@app.route('/completedbooks/<id>')
def completedBooks(id):
    book = BookList.query.filter_by(id=int(id)).first()
    book.complete = True
    db.session.commit()
    app.logger.info('Book successfully marked as complete')
    return redirect(url_for('booklist'))

