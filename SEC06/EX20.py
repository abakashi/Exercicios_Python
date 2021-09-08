num = 0
cont = 0
pares = []
while num != 1000:
    num = int(input('Insira um número: '))
    cont += 1
    if num % 2 == 0:
        pares.append(num)
print(f'Total de {cont} entradas.')
print(f'Números pares: {pares}')
