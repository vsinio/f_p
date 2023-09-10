"""Задание №3
Погружение в Python | Коллекции
✔ Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа"""

cort = ("Hello", 5, 5, 4, 3, 5.44, 5.55, "world!", (1,2,3), (2,3,4))
book = {}
lst = []


for i in cort:
    if type(i) not in book:
        book[type(i)] = []
    book[type(i)].append(i)


print(book)
