press = input("press the words or symbolds to check them: ")
if press.isdigit():
    new_press = int(press)
    print(bin(new_press), hex(new_press), oct(new_press))
else:
    print(press.isascii())
