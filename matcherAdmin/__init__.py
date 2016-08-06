"""
The flask application package.
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(os.environ.get('DATABASE_URL'))

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from matcherAdmin.models import User
# Flask-Admin Section
admin = Admin(app, name='wordmatcher', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))


import matcherAdmin.views
