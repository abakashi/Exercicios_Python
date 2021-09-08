def soma_coluna(matriz, coluna):
    soma = [i[coluna] for i in matriz]
    return sum(soma)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(soma_coluna(matriz, 0))
