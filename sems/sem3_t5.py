"""✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы."""
from random import randint

lst = [randint(0, 10) for _ in range(10)]
print(f"first full list {lst}")

lst_dig = []

for i in range(len(lst)):
    if lst[i] % 2 == True and lst[i] != True:
        lst_dig.append(i + 1)
        print(f"number(not index) = {i + 1}; value = {lst[i]}")
print(f"list with the digits: {lst_dig}")
