"""add MachineUsers FK

Revision ID: afb154b31046
Revises: 9dd78c6c2e3b
Create Date: 2017-05-21 21:46:33.098707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'afb154b31046'
down_revision = '9dd78c6c2e3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('machine_users_machine_id_fkey', 'machine_users', type_='foreignkey')
    op.create_foreign_key(None, 'machine_users', 'machine', ['machine_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'machine_users', type_='foreignkey')
    op.create_foreign_key('machine_users_machine_id_fkey', 'machine_users', 'machine', ['machine_id'], ['id'])
    # ### end Alembic commands ###
