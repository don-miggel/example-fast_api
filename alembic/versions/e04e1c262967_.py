"""empty message

Revision ID: e04e1c262967
Revises: 
Create Date: 2022-07-22 12:54:26.427750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e04e1c262967'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('notes', sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
                             sa.Column('title', sa.String())   )


def downgrade() -> None:
    op.drop_table('notes')

