def soma_diagonais(matriz):
    soma_dp = []
    soma_ds = []
    for i in range(len(matriz)):
        for j, valor in enumerate(matriz[i]):
            if i == j:
                soma_dp.append(valor)
    l = 0
    for k in range(len(matriz) -1, -1, -1):
        soma_ds.append(matriz[k][l])
        l += 1
    return sum(soma_dp), sum(soma_ds)


matriz = [[2, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(soma_diagonais(matriz))