valores = []
for i in range(5):
    entrada = int(input(f'Insira um número: '))
    valores.append(entrada)
print(f'{min(valores)} é o menor valor e está na posição {valores.index(min(valores))}.')
print(f'{max(valores)} é o maior valor e está na posição {valores.index(max(valores))}.')
