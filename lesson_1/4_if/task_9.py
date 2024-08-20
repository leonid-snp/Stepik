#!/usr/bin/python3

"""
Напишите программу, которая считывает три числа
и подсчитывает сумму только положительных чисел.
"""

# Задача
"""
4
-22
1

5
"""

# Решение
# summ = 0
# for i in range(3):
#     num = int(input())
#     if num > 0:
#         summ += num
# print(summ)

print(sum([max(0, i) for i in [int(input()) for _ in 'abc']]))