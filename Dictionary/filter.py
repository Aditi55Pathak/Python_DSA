def filter_dict(original_dict, condition):
    filtered_dict = {
        key: value for key, value in original_dict.items() if condition(key, value)
    }
    return filtered_dict


# Example usage:
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)


print(filtered_dict)
