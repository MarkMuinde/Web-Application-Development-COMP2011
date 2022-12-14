from flask import render_template,flash
from app import app
from .forms import CalculatorForm

@app.route('/')
def index():
    return "Hello World"

@app.route('/template')
def templateExample():
    user = {'name': 'Mark Muinde'}
    return render_template('index.html',
                           title='Simple template example',
                           user=user)

@app.route('/fruit')
def displayFruit():
    fruits = ["Apple", "Banana", "Orange", "Kiwi"]
    return render_template("fruit.html",fruits=fruits)

@app.route('/fruitextension')
def displayFruitExtension():
    fruits = ["Apple", "Banana", "Orange", "Kiwi"]
    return render_template("fruitextension.html",fruits=fruits)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        flash('Succesfully received form data. %s + %s  = %s'%(form.number1.data, form.number2.data, form.number1.data+form.number2.data))
    return render_template('calculator.html',
                           title='Calculator',
                           form=form)


