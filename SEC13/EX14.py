from formulas import calcula_idade

nome = input('Insira o seu nome: ')
idade = []
for i in range(3):
    dado = None
    if i == 0:
        dado = 'dia'
    elif i == 1:
        dado = 'mês'
    elif i == 2:
        dado = 'ano (AAAA)'
    entrada = idade.append(int(input(f'Insira o {dado} da sua data de nascimento: ')))

calcula_idade(nome, idade)