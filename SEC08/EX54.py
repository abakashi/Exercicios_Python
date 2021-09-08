def soma_elementos(mat):
    soma = []
    for i in range(len(mat)):
        for j, valor in enumerate(mat[i]):
            soma.append(valor)
    resul = sum(soma)
    return resul


