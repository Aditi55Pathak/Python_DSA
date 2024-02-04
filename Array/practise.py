import array

# Create an user input array and traverse it
# arr1 = input("Enter array :- ").split(",")
# print(arr1)


# Traversing array
# def traversing_array(array):
#     for i in array:
#         print("Traversing the array", i)
#     print("Length of this array", len(arr1))


# traversing_array(arr1)


# Access individual elements through index
# def access_element(array, index):
#     for i in range(len(array)):
#         if array[i] == index:
#             return i
#     return -1


# search = input("Enter element you want to search : ")
# index = access_element(arr1, search)
# if index != -1:
#     print("Yes Element is present !")
# else:
#     print("Sorry for your loss")


# Appending any value to array using append() method


# def append_value(array, value):
#     array.append(value)


# append_here = input("Enter value you want to append to array : ")
# append_value(arr1, append_here)
# print(arr1)


# Array insertion

# insert_me = input("Enter index and value : ").split(",")
# index, value = map(int, insert_me)
# arr1.insert(index, value)
# print(arr1)

# Extend elements

# extra_elements = [12, 46, 89, 56]
# arr1.extend(extra_elements)
# print("Array after extending:", arr1)

# fromlist()

# list1 = [12, 45, 6, 88]
# arr1.fromlist(list1)
# print(arr1)

# remove
remove_me = [1, 4, 6, 8, 9]
remove_me.remove(6)
print("Array after deletion:", remove_me)

# Pop element from array
pop_me = [1, 4, 6, 8, 9]
pop_me.pop()
print("Array after poping : ", pop_me)

# use index() method

Fetch_me = [1, 4, 6, 8, 9]
index_of = Fetch_me.index(4)
print("Fetched value : ", index_of)

# Reverse array

arr1 = [1, 4, 6, 8, 9]
arr1.reverse()
print("Reversed array : ", arr1)

# Buffer info
arr = array.array("i", [1, 2, 3, 4, 5])

buffer_info = arr.buffer_info()

print("Buffer info:", buffer_info)

# Count
element_count = [1, 4, 6, 8, 9]
count_here = element_count.count(6)
print(count_here)


# tostring()
element_list = [1, 4, 6, 8, 9]

# Convert list to string using join() method
element_string = "".join(map(str, element_list))

print("Converted list to string: ", element_string)

# python list

element_array = array.array('i', [1, 4, 6, 8, 9])
con=element_array.tolist()
print("Python list: ",con)

