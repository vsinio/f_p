"""Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все
операции поступления и снятия средств в список.
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю ОК✔
✔ Допустимые действия: пополнить, снять, выйти ОК✔
✔ Сумма пополнения и снятия кратны 50 у.е. ОК✔
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е. ОК✔
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3% ОК✔
✔ Нельзя снять больше, чем на счёте ОК✔
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой ОК✔
операцией, даже ошибочной ОК✔
✔ Любое действие выводит сумму денег ОК✔
"""
from pprint import pp

def pp_money(money):
    print(f"Ваш баланс равен: {money}")


def make_dep(money):
    """пополнить счет"""
    money_dep = int(input("Введите число кратное 50, чтобы пополнить счет: "))
    while money_dep % 50 != 0:
        money_dep = int(input("Вы ошиблись, введите число кратное 50 : "))
    return money_dep


def take_off(money):
    """снять деньги"""
    comission = 0.015
    money_dep = int(input("Введите число кратное 50, чтобы снять деньги со счета: "))
    while money_dep % 50 != 0:
        money_dep = int(input("Вы ошиблись, введите число кратное 50 : "))
    if money_dep * comission < 30:
        total_com = 30
    elif money_dep * comission > 600:
        total_com = 600
    else:
        total_com = money_dep * comission
    print(f"Вы сняли с вашего счета {money_dep} + комиссия {total_com}")
    return money_dep + total_com


def rich_nalog(money):
    if money > 5_000_000:
        money *= 0.9
        print(f"Упс...Налог на богатство..Ваш баланс уменьшен на 10%..извините\nБаланс: {money}")
    return money

balans_lst = [] #все балансы
action = 0  # выбор
money = 1000000  # начальная сумма
count = 0  # счетчик действий
while action != 4:
    balans_lst.append(money)
    action = int(input("Введите цифру 1 - Пополнить, 2 - Снять, 3 - вывести список всех предыдущих балансов, 4 - выйти : "))
    if action == 1:
        money = make_dep(money) + money
    pp_money(money)
    money = rich_nalog(money)
    if action == 4:
        pp(balans_lst)
    if action == 2:
        TAKE = take_off(money)
        money = money - TAKE
        if money < 0:
            print("Вы попытались обмануть банкомат? У вас нет столько денег на счету! Попытка не удалась :(")
            money += TAKE
            print(f"На счет вернулось {TAKE} включая комиссию.")
        money = rich_nalog(money)
    count += 1
    if count % 3 == 0:
        money *= 1.03
        print(f"Проценты! Вам добавилось 3% на счет, поздравляем!")
        pp_money(money)
