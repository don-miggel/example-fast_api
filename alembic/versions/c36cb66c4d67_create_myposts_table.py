"""create myposts table

Revision ID: c36cb66c4d67
Revises: 9b0c41df36ad
Create Date: 2022-07-22 13:48:37.644030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c36cb66c4d67'
down_revision = '9b0c41df36ad'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('myposts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass