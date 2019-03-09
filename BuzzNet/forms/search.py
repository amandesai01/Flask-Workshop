from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class SearchForm(FlaskForm):
    SearchQuery = StringField('Query')
    submit = SubmitField('Search')
