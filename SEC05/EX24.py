cnt = 1
while cnt == 1:
    preco = float(input('Insira o valor do produto: '))
    op = int(input('\nInsira a opção desejada:\n'
                   '1 - Minas Gerais;\n'
                   '2 - São Paulo;\n'
                   '3 - Rio de Janeiro;\n'
                   '4 - Mato Grosso do Sul.\n'
                   'Opção: '))
    if op == 1:
        pf = preco + (preco * 0.07)
        print(f'Tributado em Minas Gerais: R$: {pf:.2f}')
        cnt = int(input('Deseja continuar? (0 - não; 1 - sim).\n'))
    elif op == 2:
        pf = preco + (preco * 0.12)
        print(f'Tributado em São Paulo: R$: {pf:.2f}')
        cnt = int(input('Deseja continuar? (0 - não; 1 - sim).\n'))
    elif op == 3:
        pf = preco + (preco * 0.15)
        print(f'Tributado em Rio de Janeiro: R$: {pf:.2f}')
        cnt = int(input('Deseja continuar? (0 - não; 1 - sim).\n'))
    elif op == 4:
        pf = preco + (preco * 0.08)
        print(f'Tributado em Mato Grosso do Sul: R$: {pf:.2f}')
        cnt = int(input('Deseja continuar? (0 - não; 1 - sim).\n'))
    else:
        print('Valor inválido, tente de novo.')
        cnt = int(input('Reiniciar? (0 - não; 1 - sim).\n'))
