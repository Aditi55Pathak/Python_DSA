
def merge_dicts(dict1, dict2):
    new_dict={}
    for key in dict1:
        if key in dict2:
            new_dict[key]=dict1[key]+dict2[key]
        else:
            new_dict[key]=dict1[key]
    
    for key in dict2:
        if key not in new_dict:
            new_dict[key] = dict2[key]
    
    return new_dict
    
    
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
result=merge_dicts(dict1, dict2)

print(result)
                
