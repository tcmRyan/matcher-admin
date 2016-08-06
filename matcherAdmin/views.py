"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from flask_security import login_required
from matcherAdmin import app, user_datastore


@app.before_first_request
def create_user():
    user_datastore.create_user(email='ryan', password= 'changeme')


@app.route('/')
@app.route('/home')
@login_required
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
