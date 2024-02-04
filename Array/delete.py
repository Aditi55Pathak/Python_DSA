import array

my_arr1 = array.array("i", [1, 2, 3, 4, 5, 6])
print(my_arr1)
print(len(my_arr1))
my_arr1.remove(5)
print(my_arr1)
print(len(my_arr1))

# Time complexity deleting an number from end is O(1)
# Time complexity for deleting a number form beginning and end is O(n)
