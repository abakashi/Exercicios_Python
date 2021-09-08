numeros = []
for i in range(10):
    entrada = int(input(f'Insira o {i+1}º número: '))
    if entrada < 0:
        numeros.append(0)
    else:
        numeros.append(entrada)
print(numeros)
