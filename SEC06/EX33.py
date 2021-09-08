n = int(input('Insira a quantidade de números do conjunto: '))
i = int(input('Insira o primeiro multiplo: '))
j = int(input('Insira o segundo múltiplo: '))
vetor = []
ind = 0
if i <= 0 or j <= 0:
    print('Os dois últimos números devem ser postivos e maiores que 0.')
else:
    while len(vetor) < n:
        if ind % i == 0 or ind % j == 0:
            vetor.append(ind)
        ind += 1
    print(vetor)