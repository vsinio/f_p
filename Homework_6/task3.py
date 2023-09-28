"""Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib_gen = fibonacci_generator()

print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))