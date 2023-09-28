num = input().split("/")


def input_(num):
    fk, sk, val, *other = num
    return {fk:val, sk:other}


print(input_(num))
