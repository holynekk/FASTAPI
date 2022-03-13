"""create posts table

Revision ID: ec1a28b7b332
Revises: 
Create Date: 2022-03-13 12:51:11.537928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec1a28b7b332'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", 
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True), 
        sa.Column("title", sa.String(), nullable=False)
        )
    pass


def downgrade():
    op.drop_table("posts")
    pass
