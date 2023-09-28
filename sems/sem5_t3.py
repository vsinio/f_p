my_gen = {i for i in range(101) if i % 2 == 0 and sum(map(int, str(i))) != 8}
print(my_gen)
