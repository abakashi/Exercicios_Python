numeros = []
negativos = []
positivos = []
for i in range(10):
    entrada = int(input(f'Insira a entrada {i}: '))
    numeros.append(entrada)
    if entrada < 0:
        negativos.append(entrada)
    elif entrada > 0:
        positivos.append(entrada)
print(f'Foram detectados {len(negativos)} números negativos.')
print(f'A soma dos números positivos é {sum(positivos)}.')
print(f'Estes foram todos os números digitados:\n{numeros}.')
