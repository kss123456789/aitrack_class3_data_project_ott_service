"""empty message

Revision ID: 234740f73458
Revises: 
Create Date: 2021-12-28 16:27:22.172929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '234740f73458'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('soulmate',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_mbti', sa.String(length=10), nullable=False),
    sa.Column('soulmate_mbti', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('pw', sa.String(length=20), nullable=False),
    sa.Column('mbti', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=True),
    sa.Column('answers', sa.String(length=20), nullable=False),
    sa.Column('submitted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('option',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('mbti_indicator', sa.String(length=5), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('satisfaction',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('user_rating', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('satisfaction')
    op.drop_table('option')
    op.drop_table('answer')
    op.drop_table('user')
    op.drop_table('soulmate')
    op.drop_table('question')
    op.drop_table('movie')
    # ### end Alembic commands ###