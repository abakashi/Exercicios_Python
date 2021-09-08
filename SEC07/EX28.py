numeros = []
pares = []
impares = []
for i in range(10):
    entrada = int(input(f'Insira o {i + 1} número: '))
    numeros.append(entrada)
    if entrada % 2 == 0:
        pares.append(entrada)
    else:
        impares.append(entrada)
print(f'O vetor digitado é: \n'
      f'{numeros}\n'
      f'Destes {len(pares)} são números pares e \n'
      f'{len(impares)} são números ímpares.')
