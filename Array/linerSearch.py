arr1 = [1, 45, 67, 89, 0, 89, 65, 32, 90]


def search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1


print(search(arr1, 32))

# Time complexity: O(n)
