"""Add block_type to FinishedGood, WorkInProgress, and ProductionSchedule models

Revision ID: e24132d45f00
Revises: 3bde5190d2bb
Create Date: 2024-09-22 05:02:20.614196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e24132d45f00'
down_revision = '3bde5190d2bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('finished_good', schema=None) as batch_op:
        batch_op.add_column(sa.Column('block_type', sa.String(length=50), nullable=False))

    with op.batch_alter_table('production_schedule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('block_type', sa.String(length=50), nullable=False))

    with op.batch_alter_table('work_in_progress', schema=None) as batch_op:
        batch_op.add_column(sa.Column('block_type', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_in_progress', schema=None) as batch_op:
        batch_op.drop_column('block_type')

    with op.batch_alter_table('production_schedule', schema=None) as batch_op:
        batch_op.drop_column('block_type')

    with op.batch_alter_table('finished_good', schema=None) as batch_op:
        batch_op.drop_column('block_type')

    # ### end Alembic commands ###
