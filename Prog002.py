""" Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
seconds = int(input("Введите время в секундах: "))
minuts = seconds // 60
hours = minuts // 60
print(f"Время в формате ч:м:с - {hours} : {minuts} : {seconds}")