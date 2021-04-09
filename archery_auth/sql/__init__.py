from dotenv import load_dotenv
from os import getenv
from sqlalchemy import (
    create_engine
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

engine = create_engine(
    getenv(
        "ARCHERY_PERSON_SQL_URI"
    ),
    future=True
)
Base = declarative_base()
Session = sessionmaker(bind=engine)
