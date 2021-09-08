def identidade(m):
    diagonal = []
    elemen_0 = []
    for i in range(len(m)) :
        for j, valor in enumerate(m[i]):
            if i == j and valor != 1:
                diagonal.append(1)
            elif i != j and valor != 0:
                elemen_0.append(1)
    if len(diagonal) == 0 and len(elemen_0) == 0:
        return True
    else:
        return False

matriz = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

print(identidade(matriz))