def missingNumber(arr, n):
    num = n * (n + 1) // 2
    arr_here = sum(arr)
    sub = num - arr_here
    print(sub)


missingNumber([1, 2, 3, 4, 5, 7], 7)
