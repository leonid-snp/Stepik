#!/usr/bin/python3

"""
Напишите программу, которая принимает через стандартный поток ввода
(команда input()) три строки, а затем выводит их в обратной последовательности,
каждую на отдельной строчке.
"""

# Задача
"""
<строка1>
<строка2>
<строка3>
"""

# Решение
[print(i) for i in [input() for _ in range(3)][::-1]]
