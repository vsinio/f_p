data = [1, 4.5, 'string', 1, 4.5, True, True, 'ing']

for i in range(len(data)):
    print(f"Значение |{data[i]}|,\n |номер порядковый {i + 1}|,\n "
          f"|адрес в памяти {id(data[i])}|,\n |размер {data[i].__sizeof__()}|,\n"
          f"|хэш {hash(data[i])}|")
    if isinstance(data[i], int | float):
        print("Это число")
    else:
        print("Это не число")
    if isinstance(data[i], str):
        print("Это строка")
    else:
        print("Это не строка")
    print("*" * 100)
