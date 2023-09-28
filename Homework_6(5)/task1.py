"""✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла"""

way_to_file = "C:/Users/marke/Desktop/Firebase/BKL/file.exe"


def way(text):
    final = []
    text = text.split("/")
    counter = 1
    for item in text:
        if counter == len(text):
            continue
        final.append(item)
        counter += 1
        last_elem = text[-1]
    final = ("/").join(final)
    name_file = last_elem[:last_elem.find(".")]
    type_file = last_elem[last_elem.find(".")+1:]
    my_tup = (final, name_file, type_file)
    return my_tup


print(way(way_to_file))
