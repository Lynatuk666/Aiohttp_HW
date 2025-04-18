"""Initial revision

Revision ID: 7cc5e95a4a2b
Revises: 
Create Date: 2025-04-05 16:58:45.436735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cc5e95a4a2b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('adv')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adv',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=1000), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='adv_pkey')
    )
    # ### end Alembic commands ###
