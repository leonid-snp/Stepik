#!/usr/bin/python3

"""
Напишите программу,
которая считывает целое число и выводит для него на экран следующее
и предыдущее целые числа в следующем формате:

Следующее за числом <текущее число> число: <следующее число>
Для числа <текущее число> предыдущее число: <предыдущее число>
"""

# Задача
"""
20

21
19
"""

# Решение
a = int(input())
print(f'Следующее за числом {a} число: {a + 1}\n'
      f'Для числа {a} предыдущее число: {a - 1}')
