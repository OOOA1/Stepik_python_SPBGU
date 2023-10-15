numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

change_simbol = 4  # Меняю пропущенное число (None)

sum_numbers = sum(numbers[:change_simbol]) + sum(numbers[change_simbol + 1:])

count_numbers = len(numbers)

average_sum = sum_numbers / count_numbers
numbers[change_simbol] = average_sum
print("Измененный список:", numbers)  # Вывод ответа
