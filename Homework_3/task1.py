"""Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов."""

my_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6]
new_list = []
print(new_list)
for item in my_list:
    if item not in new_list and my_list.count(item) >= 1 and my_list.count(item) % 2 == 1:
        new_list.append(item)
print(new_list)
