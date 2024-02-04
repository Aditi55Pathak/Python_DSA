import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(arr)

num = input("Enter number you want :- ")


def findNum(arr, num):
    if num in arr:
        locations = np.where(arr == num)[0] # where to get the indices
        print("Number is present : ", num, "\nFound at location :", locations)
    else:
        print("Number not present !!")


findNum(arr, int(num))
