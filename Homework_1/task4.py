print("4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.\n"
      " Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного числа \n"
      "используйте код: from random import \ randint num = randint(LOWER_LIMIT, UPPER_LIMIT)")
from random import randint
rand_num = randint(0,1000)
print("Привет, я загадал число, у тебя есть 10 попыток, попробуй отгадать!")
counter = 10
while counter != 0:
      num = int(input("Введите число: "))
      if num == rand_num:
            print("WIN!!!!!!!")
            break
      elif rand_num < num:
            print("Число меньше!")
      elif rand_num > num:
            print("Число больше!")
      print(f"У тебя осталось {counter} попыток")
      counter-=1