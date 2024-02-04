def numberfactor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        subp1 = numberfactor(n - 1)
        subp2 = numberfactor(n - 3)
        subp3 = numberfactor(n - 4)
        return subp1 + subp2 + subp3


print(numberfactor(5))
