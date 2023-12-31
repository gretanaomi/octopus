"""empty message

Revision ID: 2d89315ac650
Revises: bc496c0a0279
Create Date: 2023-04-15 20:43:44.218020

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d89315ac650'
down_revision = 'bc496c0a0279'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_partner_subscription_end_at'), 'partner_subscription', ['end_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_partner_subscription_end_at'), table_name='partner_subscription')
    # ### end Alembic commands ###
