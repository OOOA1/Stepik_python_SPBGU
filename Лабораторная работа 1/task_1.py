numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers[4] = 0 #Здесь я присваиваю 4 значению списка numbers то есть None значение 0, что бы не получить ошибку синтаксиса
averageSum = round(sum(numbers) / len(numbers), 2) #Здесь я считаю среднее значение всех значений массива numbers что бы подставить его на место None
numbers[4] = averageSum #Здесь я присваиваю четвёртому значению списка numbers среднее значение списка

print("Измененный список:", numbers) #Вывод ответа
