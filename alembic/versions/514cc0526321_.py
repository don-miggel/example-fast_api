"""empty message

Revision ID: 514cc0526321
Revises: 57d31ca29841
Create Date: 2022-07-22 14:08:43.469586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '514cc0526321'
down_revision = '57d31ca29841'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('myposts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('mypost_users_fk', source_table="myposts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('mypost_users_fk', table_name="myposts")
    op.drop_column('myposts', 'owner_id')
    pass

