ano = int(input('Insira um ano: '))
if ano % 400 == 0:
    print('Ano bissexto.')
elif ano % 4 == 0 and ano % 100 != 0:
    print('Ano bissexto.')
else:
    print('Ano não é bissexto.')
