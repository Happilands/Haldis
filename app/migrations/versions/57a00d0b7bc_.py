"""Added order paid column

Revision ID: 57a00d0b7bc
Revises: 3243c3538fc
Create Date: 2015-06-04 19:16:47.888372

"""

# revision identifiers, used by Alembic.
revision = '57a00d0b7bc'
down_revision = '3243c3538fc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_item', sa.Column('paid', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order_item', 'paid')
    ### end Alembic commands ###