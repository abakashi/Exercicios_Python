from collections import defaultdict
numeros = []
for i in range(10):
    numeros.append(int(input(f'Insira um número: ')))
chaves = defaultdict(list)

for chave, valor in enumerate(numeros):
    chaves[valor].append(chave)

for valor in chaves:
    if len(chaves[valor]) > 1:
        print(valor, chaves[valor])
