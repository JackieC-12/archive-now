"""create archive table

Revision ID: 40637580507e
Revises: ffdc0a98111c
Create Date: 2025-01-03 23:04:53.763746

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '40637580507e'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('archives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), sa.ForeignKey("users.id")),
    sa.Column('url', sa.String(255), nullable=False),
    sa.Column('title', sa.String(25), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('fileLink', sa.String()),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")


def downgrade():
    op.drop_table('archives')
