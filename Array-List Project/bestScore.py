
def first_second(my_list):
    my_list.sort(reverse=True)
    print(my_list[0],my_list[1])
    


myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList)