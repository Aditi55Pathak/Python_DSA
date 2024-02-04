# Find the maximum product of two integers in an array where all elements are positive.

def sortHere(arr):
    arr.sort(reverse=True)
    print(arr[0]*arr[1])

arr=[1,2,3,4,5,6,7]

sortHere(arr)
