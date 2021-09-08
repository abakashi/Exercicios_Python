sal = float(input('Insira o saário R$: '))
prest = float(input('Insira o valor da prestação R$: '))
if prest < sal * 0.2:
    print('Emprestimo concedido.')
else:
    print('Empréstimo negado.')
