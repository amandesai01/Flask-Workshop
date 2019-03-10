from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class RegistrationForm(FlaskForm):
    usernames = StringField('username',
    validators=[DataRequired(),Length(min=8,max=32)])
    emails = StringField('Email',
    validators=[DataRequired(), Email()])
    passwords = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=32)])
    confirm_passwords = PasswordField('Confirm Password',
    validators = [DataRequired(), EqualTo('password')])
    submits = SubmitField('Sign Up')
