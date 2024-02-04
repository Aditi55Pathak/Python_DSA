
def sum_product(input_tuple):
    sum_result=sum(input_tuple)
    prod_res=1
    for i in range(len(input_tuple)):
        prod_res*=input_tuple[i]
    sum_pro=sum_result,prod_res
    print(sum_pro)
    
input_tuple = (1, 2, 3, 4)
sum_product(input_tuple)