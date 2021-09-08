vetor = []
for i in range(8):
    entrada = int(input(f'Insira a posição {i} do vetor: '))
    vetor.append(entrada)
x = int(input('Insira o número X: '))
y = int(input('Insira o número Y: '))
while x > len(vetor) - 1 or y > len(vetor) - 1:
    print('X e Y devem ser positivos e menores do que 8.')
    x = int(input('Insira o número X: '))
    y = int(input('Insira o número Y: '))
soma = vetor[x] + vetor [y]
print(vetor)
print(soma)
