# TODO решите задачу

import json


def task() -> float:
    with open('input.json') as check:
        data = json.load(check)

    products = [item['score'] * item['weight'] for item in data]
    total_sum = sum(products)

    return round(total_sum, 3)


print(task())

# def get_student_names(students: list[dict]) -> list[str]:
#     """Функция для извлечения списка имен учеников из списка словарей с информацией о них."""
#     return [student["name"] for student in students]
