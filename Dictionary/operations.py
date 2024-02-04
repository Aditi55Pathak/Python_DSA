dict_one = {"Company": "Sitaraman", "id": 2001}
print(dict_one)

# update
dict_one["id"] = 2002  # time complexity : O(1)
print(dict_one)

# insert

dict_one["meetings"] = "yes"  # time complexity : O(1)
print(dict_one)

# Traverse


def traverse_here(dict):
    for key in dict:  # time complexity : O(n)
        print(key, dict[key])


traverse_here(dict_one)

# Search


def search_key(dict, value):
    for key in dict:  # time complexity : O(n)
        if dict[key] == value:
            print(f"Value found : {key},{value}")
    return "Value not found!!"


search_key(dict_one, 2002)

# delete

# del dict_one['id']
# print(dict_one)

# remove_element=dict_one.pop('id')
# print(remove_element)
# print(dict_one)

# remove_element=dict_one.popitem()
# print(remove_element)
# print(dict_one)

# dict_one.clear()
# print("MyDict : ", dict_one)   --->   time complexity : O(n)

# ------> Dictionary methods   <--------

# 1) dict_one.clear()
# print("MyDict : ", dict_one)   --->   time complexity : O(n)

# 2) Copy

myDict = dict_one.copy()
print(dict_one)
print(myDict)

# 3) fromkeys

new_dict = {}.fromkeys([1, 2, 4], 6)
print(new_dict)

# 4) get

print(dict_one.get("id"), 0)

#  5) item

print(dict_one.items())

#  6) keys

print(dict_one.keys())

#  7) popitem

# remove_element=dict_one.popitem()
# print(remove_element)
# print(dict_one)

#  8) setdefault

dict=dict_one.setdefault("software","yes")
print(dict_one)

#  9) pop

# remove_element=dict_one.pop('id')
# print(remove_element)
# print(dict_one)

# 10) values

val=dict_one.values()
print(val)

# 11) Update

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)
# Updating with another dictionary
update_dict = {'b': 4, 'd': 5}
my_dict.update(update_dict)

print("Updated Dictionary:", my_dict)
