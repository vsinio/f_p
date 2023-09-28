"""✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

text = "C:/Users/marke/Desktop/lesson_4/task_3/assert.py"
def way_to_file(text):
    my_way = text.split("/")
    return my_way


print(way_to_file(text))
