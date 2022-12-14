"""adding title migration

Revision ID: 496721f4def4
Revises: 506d48ebd06e
Create Date: 2020-11-04 13:53:17.034551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '496721f4def4'
down_revision = '506d48ebd06e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('to_do_list', sa.Column('tasktitle', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('to_do_list', 'tasktitle')
    # ### end Alembic commands ###
