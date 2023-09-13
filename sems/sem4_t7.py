"""Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""
from pprint import pp
from random import randint

my_dict = {"pepsi":[randint(-500,500),randint(-500,500)],
           "coca-cola":[randint(-500,500),randint(-500,500)],
           "sprite":[randint(-500,500),randint(-500,500)]}

def money_companies(my_dict):
    for item in my_dict:
        my_dict[item] = sum(my_dict[item])
    lst = []
    for i in my_dict:
        if my_dict[i] > 0:
            lst.append(True)
    pp(my_dict)
    if len(lst) == 3:
        return True
    else:
        return False
print(money_companies(my_dict))