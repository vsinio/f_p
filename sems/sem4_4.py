"""Задание №4
✔ Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""

nums = [1, 3, 5, 2, 4, 6, 8, 7,3,2,1,23,4,5,345,6,3]

def sorting(num):
    for item in range(len(num)):
        for i in range(len(num)-1):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]

sorting(nums)
print(nums)
