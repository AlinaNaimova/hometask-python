# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n
#  = a1
#  + (n-1) * d.
# Каждое число вводится с новой строки.
#
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# Для решения этой задачи можно использовать цикл, который будет проходить
# от 1 до количества элементов в прогрессии и для каждого элемента вычислять
# по формуле a_n = a1 + (n-1) * d.


a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов в прогрессии: "))

progression = []

for i in range(n):
    progression.append(a1 + i * d)

print(progression)

