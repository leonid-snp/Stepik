#!/usr/bin/python3

"""
Напишите программу, которая определяет,
является ли год с данным номером високосным.
Если год является високосным, то выведите «YES», иначе выведите «NO».

Год является високосным, если его номер кратен
4, но не кратен 100, или если он кратен 400.
"""

# Задача
"""
2020

YES
"""

# Решение
a = int(input())
print('YES' if a % 4 == 0 and a % 100 != 0 or a % 400 == 0  else 'NO')