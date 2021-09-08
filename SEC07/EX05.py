vetor = []
pares = []
impares = []
for i in range(10):
    entrada = int(input(f'Insira a posição {i} do vetor: '))
    vetor.append(entrada)
for j in range(len(vetor)):
    if vetor[j] % 2 == 0:
        pares.append(vetor[j])
    elif vetor[j] %2 != 0:
        impares.append(vetor[j])
print(vetor)
print(pares)
print(len(pares))
print(impares)
print(len(impares))
