"""
The flask application package.
"""
import os
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin import Admin
from flask_admin import helpers as admin_helpers
from flask_admin.contrib.sqla import ModelView
from matcherAdmin.admin_model_views import AdminModelView


def ensure_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)

ALLOWED_EXTENSIONS = set(['csv'])
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ensure_dir(app.config['UPLOAD_FOLDER'])
ensure_dir(app.config['DB_FOLDER'])

from matcherAdmin.models import User, Role
# Flask-Admin Section
admin = Admin(app,
              name='wordmatcher',
              base_template= 'master_admin.html',
              template_mode='bootstrap3'
              )
admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(Role, db.session))

# Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# define a context processor for merging flask-admin's template context into the
# flask-security views
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template= admin.base_template,
        admin_view= admin.index_view,
        hasattr= admin_helpers,
        get_url= url_for
    )

import matcherAdmin.views
