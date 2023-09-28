"""✔ Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии """

names = ["John", "NeJohn", "NeNeJohn"]
moneys = [40_000, 50_000, 60_000]
prems = [10.25, 20.5, 30]


def my_gen(names, money, prem):
    my_dict = {}
    for name, money, prem in zip(names, money, prem):
        my_dict[name] = money*prem/100
    yield my_dict


print(type(my_gen(names, moneys, prems)))
print(next(my_gen(names,moneys,prems)))

#честно говоря не понял как мне в итоге сделать вывод с помощью next
#пока сдам так, а далее буду разбираться


