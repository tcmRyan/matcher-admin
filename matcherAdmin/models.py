from datetime import datetime
from matcherAdmin import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    """Authorized Users For the Word matcher 
    :param str email: email address of user
    "param str password: encrypted password for the user
    """
    __tablename__ = 'user_model'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.registered_on = datetime.utcnow()

    def is_active(self):
        """True, since we are considering all users active"""
        return True

    def get_id(self):
        """Return email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False because we don't want to allow anonymoun users"""
        return False



