def sumOfDigita(n):
    assert n >= 0 and int(n) == n, "Integer should be positive"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigita(int(n // 10))


# Testing the function
print(sumOfDigita(1234))

# We need 3 basic steps for recursion

# --> Make logic of the functon
# --> Give base condition
# --> The Constraint,unintentional criteria
