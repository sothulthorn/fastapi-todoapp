"""Create phone number for user column

Revision ID: b26dc2236c9c
Revises: 
Create Date: 2025-11-15 15:45:08.097145

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b26dc2236c9c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "phone_number",
            sa.String(length=20),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column("users", "phone_number")
