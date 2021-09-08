from formulas import anota_telefone as registrar

loop = True

while loop:
    print('Anotador de telefones.\n'
          'Insira o nome e o número do telefone da pessoa desejada.\n')
    nome = input('Insira o nome da pessoa:\n- ')
    telefone = input('Insira o telefone da pessoa:\n- ')
    registrar(nome, telefone)
    sair = input('Deseja sair? (S/N)\n- ')
    if sair.lower() == 's':
        loop = False
    else:
        continue
