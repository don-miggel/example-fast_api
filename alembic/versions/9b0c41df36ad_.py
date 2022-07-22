"""empty message

Revision ID: 9b0c41df36ad
Revises: e04e1c262967
Create Date: 2022-07-22 13:16:09.592583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b0c41df36ad'
down_revision = 'e04e1c262967'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('notes', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('notes', 'content')
