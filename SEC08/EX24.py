def asterisco(n):
    caracteres = []
    for i in range(1, 2 * n, 2):
        pos = '*' * i
        caracteres.append(pos)

    return print(*caracteres, sep='\n')


asterisco(20)
