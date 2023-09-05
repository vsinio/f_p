row = int(input())
k = row
j = 1
for _ in range(row):
    print(" " * (k - 1), "*"*j, sep="")
    k -=1
    j+=2