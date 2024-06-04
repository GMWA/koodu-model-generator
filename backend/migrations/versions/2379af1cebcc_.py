"""empty message

Revision ID: 2379af1cebcc
Revises: 30b4282c1de3
Create Date: 2024-06-03 23:33:19.330992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2379af1cebcc'
down_revision: Union[str, None] = '30b4282c1de3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('activated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'activated_at')
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###
