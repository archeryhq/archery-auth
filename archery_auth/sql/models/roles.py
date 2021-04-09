from uuid import uuid4
from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.dialects.postgresql \
    import UUID
from archery_auth.sql import Base


class Role(Base):
    """
        Role model.
    """
    __tablename__ = 'roles'
    id = Column(
        UUID(
            as_uuid=True
        ),
        primary_key=True,
        default=uuid4
    )
    name = Column(
        String(
            length=15
        ),
        nullable=False,
        unique=True
    )
    description = Column(
        String(
            length=50
        ),
        nullable=False
    )
