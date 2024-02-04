def productOfArray(arr):
    if not arr:
        return 1  # Empty array, product is 1
    else:
        return arr[0] * productOfArray(arr[1:])

# Examples
result1 = productOfArray([1, 2, 3])
result2 = productOfArray([1, 2, 3, 10])

print(result1)  # Output: 6
print(result2)  # Output: 60
