def matrica(z,x,c):
    matrix = []
    for i in range(z):
        _ = []
        for j in range(x):
            _.append(c)
        matrix.append(_)
    return matrix
matrix = matrica(3,6,5)
print(matrix)