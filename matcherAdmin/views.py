"""
Routes and views for the flask application.
"""
import os, boto3
from datetime import datetime
from flask import render_template, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
from flask_security import login_required
from matcherAdmin import app, ALLOWED_EXTENSIONS
from matcherAdmin.game_db_gen import load_from_csv
import flask_login

def allowed_file(filename):
    return '.' in filename and \
        filename.split('.', 1)[1] in ALLOWED_EXTENSIONS

def s3_upload(filename):
    filename =  filename.split('.')[0] + '.db'
    S3_BUCKET = os.environ.get('S3_BUCKET')
    s3 = boto3.client('s3')
    db_path = os.path.join(app.config.get('DB_FOLDER'), filename)
    print('DB PATH: {}, S3 Bucket: {}, filename: {}'.format(db_path, S3_BUCKET, filename)) 
    s3.upload_file(db_path, S3_BUCKET, filename)

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


@login_required
@app.route('/upload', methods=['POST'])
def upload():
    CSV_FILE = 'word_database'
    file = request.files.get(CSV_FILE, '')
    if not file:
        flash('No file part')
        return redirect(url_for('home'))    
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('home'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # load_from_csv(filename)
        # s3_upload(filename)
        upload_to_db(filename, flask_login.current_user)
        flash("Upload Complete")
    return redirect(url_for('home'))
