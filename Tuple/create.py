a = ("a", "b", "c", "d")
print(a)

# Creating a single tuple, always remember to put a comma.

b = ("a",)
print(b)

# using tuple function

c = "abcde"
d = tuple(c)
print(d)

# Traversing

for i in a:
    print(i)

# traversing through indices

for i in range(len(a)):
    print(a[i])

# Search

new_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(new_tup)


def search_here(tup, values):
    for i in range(len(tup)):
        if tup[i] == values:
            print(f"Element {values} found at location : {i}")
    return "Element not found!!"


search_here(new_tup, 7)

# Tuples and Lists

tup = (1, 42, 43, 44, 45, 6, 7, 8, 9)
lists = list(tup)
lists.insert(2, 23)
man = lists

print(tuple(man))

l = [1, 2, 3]
init_tuple = ("Python",) * (l.__len__() - l[::-1][0])

print(init_tuple)


init_tuple = ("Python") * 3

print(type(init_tuple))

# init_tuple = (1,) * 3
# init_tuple[0] = 2
# print(init_tuple)

init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))


name = "chrish"

if name == "Bob" or "Tom" or "Mike":
    print("Access Granted")
else:
    print("Acess denide")
