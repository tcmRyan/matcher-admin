from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(object):
    """Make sure the login data is clean"""
    username = StringField('name', validators=[DataRequired()])
