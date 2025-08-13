import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models_student import Base, Student


DB_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"


@pytest.fixture(scope="module")
def engine():
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)  # Создаем таблицы
    yield engine
    Base.metadata.drop_all(engine)  # Удаляем таблицы после всех тестов


@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()  # Откатываем несохраненные изменения
    session.close()
