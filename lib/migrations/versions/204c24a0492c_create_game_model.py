"""Create Game Model

Revision ID: 204c24a0492c
Revises: faebd12f9523
Create Date: 2023-05-31 12:50:04.818157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '204c24a0492c'
down_revision = 'faebd12f9523'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('platform', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###
