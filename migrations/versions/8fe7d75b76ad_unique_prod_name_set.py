"""unique prod name set

Revision ID: 8fe7d75b76ad
Revises: fd29c0e74f01
Create Date: 2021-02-11 20:45:53.847653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fe7d75b76ad'
down_revision = 'fd29c0e74f01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'report', ['product_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'report', type_='unique')
    # ### end Alembic commands ###
