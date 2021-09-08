def asterisco(n):
    caracteres = []
    for i in range(n + 1):
        pos = '*' * i
        caracteres.append(pos)
    for j in range(n - 1, 0, -1):
        pos2 = '*' * j
        caracteres.append(pos2)

    return print(*caracteres, sep='\n')


asterisco(15)
