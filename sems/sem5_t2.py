"""#Задание №2
✔ Самостоятельно сохраните в переменной строку текста.
✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
✔ Напишите преобразование в одну строку.
"""

text = "lovers of 1-st word code"

my_dict = {elem: ord(elem) for elem in text}
my_gen = ({elem: ord(elem)} for elem in text)


print(my_dict)
print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


