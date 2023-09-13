"""✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно."""
from pprint import pp

num = input("Введите два числа через пробел: ")


def dictionary(text):
    dict_ = {}
    my_lst = text.split()
    my_lst = list(map(int, my_lst))
    print(f"Вы ввели два числа 1. {min(my_lst)}, 2.{max(my_lst)}")
    for item in range(min(my_lst), max(my_lst) + 1):
        dict_[item] = chr(item)
    return dict_


pp(dictionary(num))
