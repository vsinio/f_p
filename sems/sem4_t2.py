"""✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""
from pprint import pp

def unique_code(text):
    my_lst = list(set(list(text)))
    my_lst.sort(reverse=True)
    result = []
    for item in my_lst:
        result.append(ord(item))
    return result

pp(unique_code("qwertyuiop123456789"))

