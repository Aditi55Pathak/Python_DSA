
def insert_value_front(input_tuple, value_to_insert):
    tup_list=list(input_tuple)
    tup_list.insert(0,value_to_insert)
    tup_again=tup_list
    print(tuple(tup_again))
    
input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
