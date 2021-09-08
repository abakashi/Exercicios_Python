num = int(input('Insira um número inteiro: '))
if num % 3 == 0:
    print(f'{num} é divisível por 3!')
elif num % 5 == 0:
    print(f'{num} é divisível por 5!')
else:
    print(f'{num} não é divisível nem por 3 nem por 5.')
