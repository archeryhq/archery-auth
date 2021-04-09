from uuid import uuid4
from datetime import datetime
from sqlalchemy import (
    Column,
    ForeignKey,
    Boolean,
    String,
    DateTime
)
from sqlalchemy.dialects.postgresql \
    import UUID
from archery_auth.sql import Base


class Person(Base):
    """
        Person model.
    """
    __tablename__ = "persons"
    id = Column(
        UUID(
            as_uuid=True
        ),
        primary_key=True,
        default=uuid4
    )
    email = Column(
        String(
            length=50
        ),
        nullable=False,
        unique=True
    )
    username = Column(
        String(
            length=25,
        ),
        nullable=False,
        unique=True
    )
    password = Column(
        String(
            length=45,
        ),
        nullable=False
    )
    role = Column(
        String(
            length=140,
        )
    )
    create_in = Column(
        DateTime(),
        default=datetime.now()
    )
    enabled = Column(
        Boolean(),
        default=False
    )
