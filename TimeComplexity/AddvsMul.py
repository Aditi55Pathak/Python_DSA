def dothis(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


# dothis(5, 10)

#  and space complexity will be O(1) when we have no extra space used
#  In the above code, time complexity is O(a+b) because there
# are two loops
# running one after another.


def dothat(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


dothat(5, 10)

# here time complexity is O(a*b) as loops are nested
