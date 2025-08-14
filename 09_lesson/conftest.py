import pytest
from sqlalchemy.orm import sessionmaker


DB_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"


@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()  # Откатываем несохраненные изменения
    session.close()
