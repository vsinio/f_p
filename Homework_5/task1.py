""" Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя»."""
num = int(input("Введите кол-во простых чисел, которое вам нужно: "))


def gen(number):
    def simple_num(num):
        del_num = 1
        count = 0
        for i in range(1, num):
            if num % del_num == 0:
                count += 1
            del_num += 1
        if count == 1:
            return num

    RAISE = 100  # Ограничение
    for item in range(2, RAISE):
        if item == simple_num(item):
            yield item


my_gen = gen(num)

cnt = 1  # для вывода переменная(скоро разберусь с enumerate)
for i in range(num):
    print(f"Число #{cnt} = {next(my_gen)}")
    cnt += 1
