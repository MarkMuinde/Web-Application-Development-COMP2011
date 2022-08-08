from flask import render_template, flash, request, redirect, url_for
from app import app
from app.models import ToDoList
from app import db
from .forms import TaskForm


#home page
@app.route('/')
def toDoList():
    form = TaskForm()
    incomplete = ToDoList.query.filter_by(complete=False).all()
    complete = ToDoList.query.filter_by(complete=True).all()
    return render_template('task.html', title='Simple to-do list', incomplete=incomplete, 
                                        complete=complete, form=form)

#route for creating titles
@app.route('/createtask', methods=['GET', 'POST'])
def createTask():
    form = TaskForm()
    incomplete = ToDoList.query.filter_by(complete=False).all()
    complete = ToDoList.query.filter_by(complete=True).all()
    t = ToDoList(tasktitle=form.title.data, description=form.task.data,
                 deadline=form.date.data, complete=False)
    db.session.add(t)
    db.session.commit()
    return redirect(url_for('toDoList'))

#route for completed tasks
@app.route('/completedtasks/<id>')
def completedTasks(id):
    task = ToDoList.query.filter_by(id=int(id)).first()
    task.complete = True
    db.session.commit()
    return redirect(url_for('toDoList'))


