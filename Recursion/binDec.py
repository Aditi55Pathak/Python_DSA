def decimal(n):
    assert int(n) == n, "Integer should be positive"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal(int(n / 2))


print(decimal(10))
