# Задача 18: Требуется найти в массиве A[1..N] самый близкий
# по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка
# содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random
n = int(input())
a = [random.randint(1, 10) for _ in range(n)]
print(a)
x = int(input())

closestNum = a[0]
for i in range(n):
    if abs(a[i] - x) < abs(closestNum - x):
        closestNum = a[i]

print(closestNum)
