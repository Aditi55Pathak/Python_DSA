def common_elements(tuple1, tuple2):
    common_elements_list = []

    for element in tuple1:
        if element in tuple2:
            common_elements_list.append(element)

    return tuple(common_elements_list)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)


# or

def common_elements(tuple1, tuple2):
    set1 = set(tuple1)
    set2 = set(tuple2)
    common_elements_set = set1.intersection(set2)
    return tuple(common_elements_set)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)


# or

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))