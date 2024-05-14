"""medico tem especilialidade

Revision ID: f0de61dbae5b
Revises: 768c1795a51d
Create Date: 2024-05-14 20:52:45.790913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0de61dbae5b'
down_revision = '768c1795a51d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('especialidade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('medico',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.Column('fk_especialidade_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_especialidade_id'], ['especialidade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('medico')
    op.drop_table('especialidade')
    # ### end Alembic commands ###
