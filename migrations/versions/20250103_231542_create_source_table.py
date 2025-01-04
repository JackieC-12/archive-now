"""create source table

Revision ID: facc32db5627
Revises: 40637580507e
Create Date: 2025-01-03 23:15:42.884700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'facc32db5627'
down_revision = '40637580507e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('sources',
    sa.Column('archiveId', sa.Integer, sa.ForeignKey('archives.id'), nullable=False),
    sa.Column('fileLink', sa.String),
    sa.Column('rawHTML', sa.String, nullable=False),
    sa.Column('time_created', sa.DateTime)
    )


def downgrade():
    op.drop_table('sources')
