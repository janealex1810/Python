from models_student import Student


def test_create_student(session):
    # Подготовка тестовых данных
    test_student = Student(
        name="Иван Иванов",
        email="ivan@example.com"
    )

    # Выполнение операции
    session.add(test_student)
    session.commit()

    # Проверка результатов
    created_student = session.query(Student).filter_by(email="ivan@example.com").first()

    assert created_student is not None
    assert created_student.name == test_student.name
    assert created_student.is_active is True

    # Очистка после теста
    session.delete(created_student)
    session.commit()
