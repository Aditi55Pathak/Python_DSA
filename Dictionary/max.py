def max_value_key(my_dict):
    max_val = max(my_dict.values())

    for key, val in my_dict.items():
        if val == max_val:
            return key


my_dict = {"a": 5, "b": 9, "c": 2}
result = max_value_key(my_dict)

print(result)
