"""
Postgres models for the matcherAdmin application
"""


from matcherAdmin import db
from flask_security import UserMixin, RoleMixin


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    """
    Roles for authorization.
    """
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name
 

class User(db.Model, UserMixin):
    """Authorized Users For the Word matcher
    :param str email: email address of user
    "param str password: encrypted password for the user
    """

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    active = db.Column(db.Boolean, default=False)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role',
                            secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email

class Gamedata(db.Model):
    """ 
    Table to host all the matches for the word matcher admin.
    """
    id = db.Column(db.Integer, primary_key=True, unique=True)
    game_table_id = db.Column(db.Integer, db.ForeignKey('gametable.id'))
    wordBase = db.Column(db.String)
    combination = db.Column(db.String)
    result = db.Column(db.String)
    __tablename__ = 'gamedata'
    __table_args__ = (db.UniqueConstraint('base', 'combination', name='_base_combination'),)

    def to_json(self):
        return {
            'wordBase': self.base,
            'combination': self.combination,
            'result': self.result
        }


class Gametable(db.Model):
    """
    Table managing the connections to the tables
    """

    id = db.Column(db.Integer, primary_key=True,  unique=True)
    table = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    description = db.Column(db.LargeBinary)
    seed = db.Column(db.String) 
    data = db.relationship('Gamedata', backref='gametable', cascade='all, delete-orphan', lazy='dynamic')

    __tablename__ = 'gametable'
    __table_args__ = (db.UniqueConstraint('table', 'author', name='_author_table'),)
