"""add user table

Revision ID: 8386c4343301
Revises: eb8e8b8c55b1
Create Date: 2022-03-13 13:23:38.746704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8386c4343301'
down_revision = 'eb8e8b8c55b1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", 
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
