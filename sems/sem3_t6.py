a = "per aspera ad astra"
lst = sorted(a.split(" "))
len_max = max(lst,key=len)
len_max = len(len_max)+1
for ham,eggs in enumerate(lst,1):
    print(f"{ham}.{eggs : >{len_max}}")

print(len_max)
print(lst)
