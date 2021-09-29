from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

# class NewBookForm(FlaskForm):
#     title = StringField("Title", validators=[DataRequired()])
#     rating = SelectField("Rating", choices=["New favorite", "Great", 
#                                     "Good", "Underwhelming", 
#                                     "Bad", "Horrible"])
#     submit = SubmitField("Add Book")

class LoginForm(FlaskForm):
    employee_number = StringField("Employee Number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    
