arr1 = [1, 45, 67, 89, 0, 89, 65, 32, 90]


def access_array(array, index):
    if index > len(array):
        print("Array out of Bound !")
    else:
        print(array[index])


access_array(arr1, 1)


#  Time complexity:- O(1)
