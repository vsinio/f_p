num = int(input("Введите число:"))
degree = int(input("Введите степень в которую надо перевести: "))

text = ""
print(bin(num))
print(oct(num))
print(hex(num))
while num != 0:
    ost = num % degree
    text = str(ost) + text
    num = num // degree
print(text)
