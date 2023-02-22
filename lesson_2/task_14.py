# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())
integer_degrees = 1
while integer_degrees < n:
    if integer_degrees < n:
        if integer_degrees * 2 > n:
            break
        else:
            integer_degrees = integer_degrees * 2
            print(integer_degrees)
