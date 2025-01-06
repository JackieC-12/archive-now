"""create comments table

Revision ID: d9420d5422d7
Revises: 40637580507e
Create Date: 2025-01-06 01:24:58.352559

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'd9420d5422d7'
down_revision = '40637580507e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), sa.ForeignKey("users.id")),
    sa.Column('archiveId', sa.Integer(), sa.ForeignKey("archives.id")),
    sa.Column('message', sa.String(255), nullable=False),
    sa.Column('created_at', sa.DateTime),
    sa.PrimaryKeyConstraint('id')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")


def downgrade():
    op.drop_table('comments')
