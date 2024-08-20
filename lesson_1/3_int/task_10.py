#!/usr/bin/python3

"""
Геометрической прогрессией называется последовательность чисел b1, b2, ... bn,
каждое из которых, начиная с b2 получается из предыдущего умножением на одно
и то же постоянное число q (знаменатель прогрессии).

Если известен первый член прогрессии и ее знаменатель, то
n-ый член геометрической прогрессии находится по формуле

bn = b1 * q^n-1
"""

# Задача
"""
1
2
5

16
"""

# Решение
b1, q, n = int(input()), int(input()), int(input())
print(b1 * q ** (n - 1))