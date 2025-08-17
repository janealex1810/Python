from models_student import Student


def test_update_student(session):
    # Создаем тестовые данные
    test_student = Student(
        name="Петр Петров",
        email="petr@example.com"
    )
    session.add(test_student)
    session.commit()

    # Ищем студента для обновления
    student_to_update = session.query(Student).filter_by(email="petr@example.com").first()

    # Убеждаемся, что студент найден
    assert student_to_update is not None, "Студент не найден для обновления"

    # Обновляем данные
    student_to_update.name = "Петр Сидоров"
    session.commit()

    # Проверяем обновление
    updated_student = session.query(Student).filter_by(email="petr@example.com").first()
    assert updated_student is not None, "Обновленный студент не найден"
    assert updated_student.name == "Петр Сидоров", "Имя студента не обновилось должным образом"

    # Очистка
    session.delete(updated_student)
    session.commit()
