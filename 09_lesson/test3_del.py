from models_student import Student


def test_hard_delete_student(session):
    # Создаем тестовые данные
    test_student = Student(
        name="Сергей Сергеев",
        email="sergey@example.com"
    )
    session.add(test_student)
    session.commit()

    # Ищем студента для удаления
    student_to_delete = session.query(Student).filter_by(email="sergey@example.com").first()
    assert student_to_delete is not None, "Студент не найден для удаления"

    # Удаляем студента
    session.delete(student_to_delete)
    session.commit()

    # Проверяем удаление
    deleted_student = session.query(Student).filter_by(email="sergey@example.com").first()
    assert deleted_student is None, "Студент не удален"


def test_soft_delete_student(session):
    # Создаем тестовые данные
    test_student = Student(
        name="Анна Аннова",
        email="anna@example.com",
        is_active=True  # Убедитесь, что статус активен
    )
    session.add(test_student)
    session.commit()

    # Ищем студента для мягкого удаления
    student_to_delete = session.query(Student).filter_by(email="anna@example.com").first()
    assert student_to_delete is not None, "Студент не найден для мягкого удаления"

    # Мягкое удаление (устанавливаем is_active=False)
    student_to_delete.is_active = False
    session.commit()

    # Проверяем мягкое удаление
    soft_deleted = session.query(Student).filter_by(email="anna@example.com").first()
    assert soft_deleted is not None, "Обновленный студент не найден"
    assert soft_deleted.is_active is False, "Статус студента не обновился должным образом"

    # Очистка: удаляем студента, если требуется
    session.delete(soft_deleted)
    session.commit()
