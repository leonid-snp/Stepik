#!/usr/bin/python3

"""
Напишите программу вывода на экран трех последовательно идущих чисел,
каждое на отдельной строке. Первое число вводит пользователь,
остальные числа вы должны сами вычислять в программе.
"""

# Задача
"""
1
2
3
"""

# Решение
num = int(input())
print(num, num + 1, num + 2, sep='\n')