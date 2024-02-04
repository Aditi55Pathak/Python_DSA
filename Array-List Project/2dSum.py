def diagonal_sum(matrix):
    sumhere = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sumhere += matrix[i][j]
    return sumhere
    
myList2D=[[1,2,3],[4,5,6],[7,8,9]]

diagonal_sum(myList2D)
