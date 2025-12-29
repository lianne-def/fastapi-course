"""add content column to post table

Revision ID: 4fb53dd3b0cc
Revises: 1e486169ff06
Create Date: 2025-12-29 14:15:15.000378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fb53dd3b0cc'
down_revision: Union[str, Sequence[str], None] = '1e486169ff06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
