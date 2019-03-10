from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class LoginForm(FlaskForm):
    emaill = StringField('Email',
    validators=[DataRequired(), Email()])
    passwordl = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=32)])
    submitl = SubmitField('login')
