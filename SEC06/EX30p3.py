n = int(input('Insira um número natural: '))
vetor = []
if n <= 0:
    print('Valor inválido: ')
else:
    for i in range(1, 2*n - 1):
        if i % 2 != 0:
            vetor.append(i)
    s = sum(vetor)
    print(s)
