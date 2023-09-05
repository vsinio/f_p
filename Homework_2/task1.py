"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""

num = int(input("Введите число для перевода в 16ичную СС: "))
print(f" Проверка hex = {hex(num)[2:]}")
ss = 16
remainder = 0
result = ""
letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

while num != 0:
    remainder = num % ss
    result = letters[remainder] + result
    num //= ss

print(f"result = {result}")
