valores = []
for i in range(6):
    valores.append(int(input(f'Insira o {i + 1} número: ')))
pares = []
impares = []
for j in range(len(valores)):
    if valores[j] % 2 == 0:
        pares.append(valores[j])
    else:
        impares.append(valores[j])
print(pares)
print(f'Soma dos números pares {sum(pares)}.')
print(impares)
print(f'Quantidade de número ímpares {len(impares)}.')
