from matcherAdmin.models import User, Role
from matcherAdmin import db
from flask_security import SQLAlchemyUserDatastore

user_ds = SQLAlchemyUserDatastore(db, User, Role)

def create_role_and_admin():
    """
    Run this script to create a temporary admin user on a new db.
    """
    user_ds.find_or_create_role(name='superuser', description='Administrative Access')
    user_ds.create_user(
        email='admin',
        password='changeme',
        name='admin'
    )
    db.session.commit()
    user_ds.add_role_to_user('admin', 'superuser')
    db.session.commit()

if __name__ == '__main__':
    create_role_and_admin()