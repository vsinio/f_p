import copy
from random import randint

lst_random = []
lst_random_second = lst_random

for i in range(15):
    lst_random.append(randint(1, 15))
print(f"{lst_random = } Список с числами наугад от 1 до 15 вкл")
set_unique = set(lst_random)
print(f"{list(set_unique) = } Список с уникальными числами наугад от 1 до 15 вкл")

lst_random_unique = []
for i in lst_random_second:
    if i in lst_random_unique:
        continue
    else:
        lst_random_unique.append(i)

print(f"{lst_random_second =} Список с числами наугад от 1 до 15 вкл")
print(f"{sorted(lst_random_unique) = } Список с уникальными числами наугад от 1 до 15 вкл")
