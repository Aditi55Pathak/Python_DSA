def flatten(arr):
    result = []
    for elem in arr:
        if isinstance(elem, list):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result

# Examples
print(flatten([1, 2, 3, [4, 5]]))  # Output: [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]]))  # Output: [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]]))  # Output: [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))  # Output: [1, 2, 3]
