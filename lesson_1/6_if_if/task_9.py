#!/usr/bin/python3

"""
На числовой прямой даны два отрезка: [a1; b1] , [a2; b2]
Напишите программу, которая находит их пересечение.

Пересечением двух отрезков может быть:
"""

# Задача
"""
0

зеленый
"""

# Решение
a1, b1, a2, b2 = [int(input()) for _ in range(4)]
if b2 == a1:
    print(b2)
elif a2 < a1 and b2 < a1:
    print('пустое множество')
elif a2 < a1 and b2 < b1:
    print(a1, b2)
elif a2 < a1 and b1 <= b2:
    print(a1, b1)
elif a1 == a2 and b2 < b1:
    print(a2, b2)
elif a2 < b1 and b2 <= b1:
    print(a2, b2)
elif a2 < b1:
    print(a2, b1)
elif a2 == b1:
    print(a2)
else:
    print('пустое множество')