# Top Down


def fib(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]


dict = {}
print(fib(6, dict))

# Time complexity is O(n)

# Bottom Up


def fibBottomUp(n):
    tb = [0, 1]
    for i in range(2, n + 1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[n - 1]


print(fibBottomUp(6))

# Time complexity is O(n)