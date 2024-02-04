def fibonacci_divide_and_conquer(n):
    if n < 1:
        return "This is an error message!!"
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci_divide_and_conquer(n - 1) + fibonacci_divide_and_conquer(n - 2)


# Time Complexity : O(n^2)
