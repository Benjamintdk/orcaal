"""empty message

Revision ID: f5570f00d87d
Revises: 0ec1420e9779
Create Date: 2020-08-18 17:17:28.375163

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "f5570f00d87d"
down_revision = "0ec1420e9779"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "model",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=30), nullable=True),
        sa.Column("version", sa.Integer(), nullable=True),
        sa.Column("url", sa.String(length=100), nullable=True),
        sa.Column("accuracy", sa.Float(), nullable=True),
        sa.Column("loss", sa.Float(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("labeled_files", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("model_accuracy")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "model_accuracy",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "accuracy",
            postgresql.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "timestamp", postgresql.TIMESTAMP(), autoincrement=False, nullable=True
        ),
        sa.Column("labeled_files", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="model_accuracy_pkey"),
    )
    op.drop_table("model")
    # ### end Alembic commands ###
