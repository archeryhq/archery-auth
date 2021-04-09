from archery_auth.sql import Base, engine
from archery_auth.sql.models.roles import Role
from archery_auth.sql.models.persons import Person


def drop_tables() -> bool:
    Base.metadata.drop_all(engine)
    return True


def create_tables() -> bool:
    Base.metadata.create_all(engine)
    return True


def renew() -> bool:
    """
        Initialize database.
    """
    drop_tables()
    create_tables()
    return True
