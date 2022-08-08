from flask_wtf import Form
from wtforms import TextField
from wtforms import TextAreaField
from wtforms import DateField
from wtforms.validators import DataRequired

#creating the form classes
class BookForm(Form):
    title = TextField('title', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    date = DateField('date', format='%Y-%m-%d',validators=[DataRequired()])
   


