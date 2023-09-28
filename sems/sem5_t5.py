"""Задание №5
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
"""
lst = []
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        lst.append("FizzBuzz")
    if i % 3 == 0:
        lst.append("FIzz")
    if i % 5 == 0:
        lst.append("Buzz")
    else:
        lst.append(i)
print(lst)

fizz_buzz_generator = (
"FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Buzz" if i % 3 == 0 else "Fizz" if i % 5 == 0 else i for i in
range(1, 101))

print(next(fizz_buzz_generator))
print(next(fizz_buzz_generator))
print(next(fizz_buzz_generator))
print(next(fizz_buzz_generator))
print(next(fizz_buzz_generator))
print(next(fizz_buzz_generator))
print(next(fizz_buzz_generator))
