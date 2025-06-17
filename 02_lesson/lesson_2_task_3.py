import math


def square(side):
    """Возвращает площадь квадрата."""
    area = side * side
    return math.ceil(area)


side_length = 3.5
area_result = square(side_length)


print(f"Площадь квадрата со стороной {side_length}: {area_result}")
