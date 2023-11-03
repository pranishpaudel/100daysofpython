from flask_wtf import FlaskForm
from wtforms import SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Login')
