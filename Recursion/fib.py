def fibonaccai(n):
    assert n >= 0 and int(n) == n, "The value should be positive integer"
    if n in [0, 1]:
        return 1
    else:
        return fibonaccai(n - 1) + fibonaccai(n - 2)


print(fibonaccai(5))
