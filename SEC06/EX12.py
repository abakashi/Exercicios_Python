n = int(input('Insira um número natural diferente de zero: '))
if n<= 0:
    print('Número inválido: ')
else:
    for i in range(n, -1, -1):
        print(i)
