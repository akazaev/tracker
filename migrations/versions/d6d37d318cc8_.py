"""empty message

Revision ID: d6d37d318cc8
Revises: f1cba4163bec
Create Date: 2021-06-17 22:13:47.764512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6d37d318cc8'
down_revision = 'f1cba4163bec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracks', sa.Column('track_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tracks', 'track_id')
    # ### end Alembic commands ###
