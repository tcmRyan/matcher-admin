"""empty message

Revision ID: 68a660a65ac6
Revises: a4159d289fc7
Create Date: 2016-08-06 16:44:10.730371

"""

# revision identifiers, used by Alembic.
revision = '68a660a65ac6'
down_revision = 'a4159d289fc7'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'email')
    )
    op.drop_table('user_model')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('authenticated', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('registered_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('email', name='user_model_pkey')
    )
    op.drop_table('user')
    op.drop_table('role')
    ### end Alembic commands ###
