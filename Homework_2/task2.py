"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions."""
from fractions import Fraction

x1, x2 = int(input("1.Введите числитель:")), int(input("1.Введите знаменатель: "))
y1, y2 = int(input("2.Введите числитель:")), int(input("2.Введите знаменатель: "))

if x2 == y2:
    result_addition = f"{x1 + y1}/{x2}"
else:
    result_addition = f"{x1 * y2 + y1 * x2}/{x2 * y2}"

print(f' Сложение = {x1}/{x2} + {y1}/{y2} = {result_addition}')
print(f' Умножение = {x1}/{x2} * {y1}/{y2} = {x1 * y1}/{x2 * y2}')

print(Fraction(1, 2) + Fraction(3, 4))
print(Fraction(1, 2) * Fraction(3, 4))
