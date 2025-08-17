import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"


@pytest.fixture(scope='session')
def engine():
    """Создание SQLAlchemy engine."""
    engine = create_engine(DB_URL)
    yield engine
    # Закрываем engine после завершения тестов, если это необходимо.
    engine.dispose()


@pytest.fixture
def session(engine):
    """Фикстура для создания новой сессии."""
    Session = sessionmaker(bind=engine)
    session = Session()

    # Опционально: можно удалить данные в таблице перед тестами
    # session.query(YourModel).delete()
    # session.commit()

    yield session

    session.rollback()  # Откатываем несохраненные изменения
    session.close()
