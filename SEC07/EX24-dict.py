alturas = {}
for i in range(10):
    nome = input(f'Insira o nome do {i+1} aluno: ')
    alt = float(input(f'Insira a altura do {i+1} aluno: '))
    alturas.update({nome: alt})

print(f'{max(alturas, key=alturas.get)} é o aluno mais alto com {alturas[max(alturas, key=alturas.get)]} de altura.')
print(f'{min(alturas, key=alturas.get)} é o aluno mais baixo com {alturas[min(alturas, key=alturas.get)]} de altura.')
print(alturas)
