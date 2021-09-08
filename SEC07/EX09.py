numeros = []
for i in range(6):
    entrada = int(input(f'Insira o número par da posição {i}: '))
    while entrada % 2 != 0:
        print('O número deve ser obrigatóriamente par.')
        entrada = int(input(f'Insira o número par da posição {i}: '))
    else:
        numeros.append(entrada)
numeros.reverse()
print(numeros)
