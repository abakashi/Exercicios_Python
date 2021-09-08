def soma_abaixo_dia(mat):
    soma = []
    for i in range(len(mat)):
        for j, k in enumerate(mat[i]):
            if i > j:
                soma.append(k)
    return sum(soma)





matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(soma_abaixo_dia(matriz))
