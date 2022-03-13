"""add content column to post table

Revision ID: eb8e8b8c55b1
Revises: ec1a28b7b332
Create Date: 2022-03-13 13:17:39.923502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb8e8b8c55b1'
down_revision = 'ec1a28b7b332'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
