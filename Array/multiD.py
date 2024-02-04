import numpy as np

arr1 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 0, 1], [1, 4, 5, 6]])
print(arr1)
# Time complexity:O(nm)

# Insertion

new_arr = np.insert(arr1, 3, [[2, 6, 4, 5]], axis=1)  # 1--> row and 0 is for coloumn
# print(new_arr)

# Insertion at end without using column name or anything

new_arr = np.append(arr1, [[9, 8, 7, 6]], axis=0)
# print(new_arr)


# Acessing element


def access_elem(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array):
        print("Array out of bound")
    else:
        print(array[rowIndex][colIndex])


access_elem(arr1, 2, 3)


# Traversing


def traversing(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traversing(arr1)

# Time complexity is O(n^2)

# Searching


def searchElement(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                print("Element found at location : ", "", str(i), "", str(j))
    return "Element not found!!"


searchElement(arr1, 6)

# Time complexity: O(mn)

# Deletion

# Time complexity: O(mn)

del_arr = np.delete(arr1, 0, axis=1)
print(del_arr)
