"""Add missing Token->User foreign key

Revision ID: 12d9fa9e4227
Revises: 23ad5a12e1fb
Create Date: 2017-07-12 21:56:23.903912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12d9fa9e4227'
down_revision = '23ad5a12e1fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('token', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'token', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'token', type_='foreignkey')
    op.alter_column('token', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###