"""add content column

Revision ID: f5b5fefe335b
Revises: 8f2359f612ff
Create Date: 2022-07-22 18:59:16.596065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5b5fefe335b'
down_revision = '8f2359f612ff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('myposts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('myposts', 'content')
    pass
