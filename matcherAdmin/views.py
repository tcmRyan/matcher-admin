"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, Response, url_for
from flask_login import login_required, login_user, logout_user
from matcherAdmin import app, login_manager
from matcherAdmin.models import User
from matcherAdmin.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id, return the associated User object.
    :param unicode user_id: user_id(email) user to retrieve
    """
    return User.query.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(user)
        next = request.args.get('next')
        if not next_is_valid(next):
            return flask.abort(400)
        return redirect(next or url_for('index'))
    return render_template('login.htm', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login Failed</p>')
