def create(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
        for k in range(n):
            print(k)


# complexity of loop 1 will be O(n^2) and loop 2 will be O(n) hence total complexity
# is O(n^2+n) here drop the non dominent term that is O(n) hence final complexity
# is O(n^2)

create(10)
