def get_diagonal(input_tuple):
    diagonal_elements = []
    for i in range(len(input_tuple)):
        diagonal_elements.append(input_tuple[i][i])
    return tuple(diagonal_elements)

input_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
output_tuple = get_diagonal(input_tuple)
print(output_tuple)


# a,b="pq"
# b,c="rs"
# print(a,b,c)
