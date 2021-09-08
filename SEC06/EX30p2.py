n = int(input('Insira um número natural: '))
vetor = []
if n <= 0:
    print('Valor inválido: ')
else:
    for i in range(1, 2*n - 1):
        vetor.append(i - (i + 1))
    s = sum(vetor)
    print(s)
