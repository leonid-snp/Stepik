#!/usr/bin/python3

"""
Даны три различных целых числа. Напишите программу,
которая находит серединное значение из этих чисел.

Формат входных данных
На вход программе подаются три различных целых числа, каждое на отдельной строке.
"""

# Задача
"""
1
2
3

2
"""

# Решение
print(sorted([int(input()) for _ in range(3)])[1])
