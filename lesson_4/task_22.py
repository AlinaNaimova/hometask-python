# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
#
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
import random

n = (int(input("Введите число N элементов: ")))
num_list_1 = [random.randint(1, 20) for _ in range(n)]
print(num_list_1)


m = (int(input("Введите число M элементов: ")))
num_list_2 = [random.randint(1, 20) for _ in range(m)]
print(num_list_2)

num_list3 = num_list_1+num_list_2
print(num_list3)
for i in set(num_list3): #используется цикл for, чтобы пройтись по всем уникальным элементам списка.
    if num_list3.count(i) > 1: #проверяем, сколько раз каждый уникальный элемент встречается в списке. Если он встречается больше одного раза, то он выводится на экран.
        print(i)
