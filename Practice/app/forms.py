from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired

class CalculatorForm(Form):
    number1 = IntegerField('number1', validators=[DataRequired()])
    number2 = IntegerField('number2', validators=[DataRequired()])