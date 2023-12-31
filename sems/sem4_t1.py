"""✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки."""

def reformat(text):
    my_lst = text.split()
    my_lst.sort()
    len_ = len(max(my_lst, key=len))
    print("Отсортированный по Unicode текст:")
    for item in range(len(my_lst)):
        print(f"{item+1}.{my_lst[item] : >{len_+1}}")
    

reformat("длинного слова был один пробел между ним и номером строки")

