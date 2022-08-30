from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from awidgets.core.constants import SQLALCHEMY_DATABASE_URI

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Generator[Session, Any, None]:
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
