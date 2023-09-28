# Генераторная строка представляющая таблицу умножения
multiplication_table = '\n'.join(f'{i}x{j}={i*j}' for i in range(2, 10) for j in range(2, 11))

# Вывод результата
print(multiplication_table)