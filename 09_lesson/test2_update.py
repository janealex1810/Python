from models_student import Student


def test_update_student(session):
    # Создаем тестовые данные
    test_student = Student(
        name="Петр Петров",
        email="petr@example.com"
    )
    session.add(test_student)
    session.commit()

    # Обновляем данные
    student_to_update = session.query(Student).filter_by(email="petr@example.com").first()
    student_to_update.name = "Петр Сидоров"
    session.commit()

    # Проверяем обновление
    updated_student = session.query(Student).filter_by(email="petr@example.com").first()
    assert updated_student.name == "Петр Сидоров"

    # Очистка
    session.delete(updated_student)
    session.commit()
