
def reverse_dict(my_dict):
    rev_dict={values:key for key,values in my_dict.items()}
    return rev_dict


my_dict = {'a': 1, 'b': 2, 'c': 3}
res=reverse_dict(my_dict)

print(res)