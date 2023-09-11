"""✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях."""
from pprint import pp


text = "Привет привет как твои дела, друг?,,,,,"
dict = {}
list_with_words = set(text)
for item in list_with_words:
    dict[item] = text.count((item))



"""for i in text:
    if i not in list_with_words:
        list_with_words.append(i)
for j in list_with_words:
    if list_with_words.count(j) > 1:
        del[j]
for k in list_with_words:
    if k not in dict:
        dict[k] = text.count(k)"""
print(list_with_words)
pp(dict)
