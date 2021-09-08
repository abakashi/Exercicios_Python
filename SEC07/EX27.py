numeros = []
fatores = []
for i in range(10):
    numeros.append(int(input('Insira um número inteiro: ')))
for i in range(len(numeros)):
    ind = numeros[i]
    if ind != 1 and ind > 0:
        for j in range(1, ind + 1):
            if ind % j == 0:
                fatores.append(j)
        if len(fatores) <= 2:
            print(f'{ind} é primo e está na posição {i} do vetor.')
    fatores.clear()

print(numeros)
