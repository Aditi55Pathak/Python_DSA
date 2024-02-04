def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linearSearch([1,5,2,7,9],9))
