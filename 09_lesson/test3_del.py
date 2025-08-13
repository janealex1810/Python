from models_student import Student


def test_hard_delete_student(session):
    # Создаем тестовые данные
    test_student = Student(
        name="Сергей Сергеев",
        email="sergey@example.com"
    )
    session.add(test_student)
    session.commit()

    # Удаляем студента
    student_to_delete = session.query(Student).filter_by(email="sergey@example.com").first()
    session.delete(student_to_delete)
    session.commit()

    # Проверяем удаление
    deleted_student = session.query(Student).filter_by(email="sergey@example.com").first()
    assert deleted_student is None


def test_soft_delete_student(session):
    # Создаем тестовые данные
    test_student = Student(
        name="Анна Аннова",
        email="anna@example.com"
    )
    session.add(test_student)
    session.commit()

    # Мягкое удаление (устанавливаем is_active=False)
    student_to_delete = session.query(Student).filter_by(email="anna@example.com").first()
    student_to_delete.is_active = False
    session.commit()

    # Проверяем мягкое удаление
    soft_deleted = session.query(Student).filter_by(email="anna@example.com").first()
    assert soft_deleted is not None
    assert soft_deleted.is_active is False

    # Очистка
    session.delete(soft_deleted)
    session.commit()
