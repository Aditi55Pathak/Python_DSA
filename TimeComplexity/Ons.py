def create(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


create(10)  # Here time complexity will be big O(n^2) only because O(n^3) or anything
#  is reported as big O(n^2) only
