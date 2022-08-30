from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from awidgets.main import app
from awidgets.models import Base
from awidgets.services.db import get_db_session

SQLALCHEMY_DATABASE_URL = "sqlite:///./db/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="session")
def db_session() -> Generator:
    yield TestingSessionLocal()


def override_get_db_session():
    db_test_session = TestingSessionLocal()
    try:
        yield db_test_session
    finally:
        db_test_session.close()


app.dependency_overrides[get_db_session] = override_get_db_session
