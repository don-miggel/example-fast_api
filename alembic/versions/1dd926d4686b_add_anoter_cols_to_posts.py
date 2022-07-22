"""add anoter cols to posts

Revision ID: 1dd926d4686b
Revises: c36cb66c4d67
Create Date: 2022-07-22 13:52:16.113086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dd926d4686b'
down_revision = 'c36cb66c4d67'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('myposts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('myposts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('myposts', 'published')
    op.drop_column('myposts', 'created_at')
    pass