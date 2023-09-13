"""✔ Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии"""
my_str = ["Anastasia", "Ivan", "Egor"]
my_int = [1, 5, 10]
my_prem = ["10.25%", "20.50%", "30.15%"]

def salary(my_str, my_int, my_prem):
    my_dict = {}
    my_prem = list(map(lambda x: x.replace("%", ''), my_prem))
    my_prem = list(map(float, my_prem))
    new_lst = []
    for item in range(len(my_int)):
        new_lst.append(my_int[item]*my_prem[item])
    my_dict = dict(zip(my_str, new_lst))
    return my_dict
print(salary(my_str,my_int,my_prem))


