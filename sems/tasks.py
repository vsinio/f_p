#Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
result = 0
result_second = 0
END = 10
num_e = int(input())
cnt = 1
ODD = 0
ODD_second = 0
while cnt != END:
    if cnt%2==0 and cnt%num_e!=0:
        ODD+=1
        result+=cnt
    cnt += 1
print(f"Нечетных чисел делящихся на {num_e} от 1 до {END} - {ODD}")
print(f"сумма = {result}")

for i in range(1,END):
    if i%2==0 and i%num_e!=0:
        ODD_second+=1
        result_second += i

print(f"Нечетных чисел делящихся на {num_e} от 1 до {END} - {ODD}")
print(f"сумма = {result_second}")
