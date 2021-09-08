def transposta(matriz):
    v_temp = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            v_temp.append(matriz[j][i])
    transp = []
    z = 0
    while z < len(v_temp):
        transp.append(v_temp[z:z+len(matriz)])
        z += len(matriz)
    return transp


mat = [[1, 2], [3, 4]]
print(transposta(mat))