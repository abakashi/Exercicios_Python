meow = int(input('Insira um número inteiro positivo: '))
vetozinho = []
if meow <= 0:
    print('Número inválido.')
else:
    for minhal in range(1, meow + 1):
        vetozinho.append(1/minhal)
med_harm = sum(vetozinho)
print(med_harm)
