def maior_10(mat):
    maior_ten = []
    for i in range(len(mat)):
        for j in mat[i]:
            if j > 10:
                maior_ten.append(j)
    return len(maior_ten)





matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10 , 11, 12], [13, 14, 15, 16]]
print(maior_10(matriz))
