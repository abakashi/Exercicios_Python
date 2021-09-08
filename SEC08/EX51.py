def soma_dia_sec(mat):
    soma = []
    j = 0
    for i in range(len(mat) - 1, -1, -1):
        soma.append(mat[i][j])
        j += 1
    return sum(soma)






matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(soma_dia_sec(matriz))
