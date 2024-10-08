"""empty message

Revision ID: d69e73030b43
Revises: 5712e3bfac4c
Create Date: 2024-08-28 16:37:05.157159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd69e73030b43'
down_revision = '5712e3bfac4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=140), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('summary', sa.String(length=140), nullable=True),
    sa.Column('featured_image', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_post')
    # ### end Alembic commands ###
