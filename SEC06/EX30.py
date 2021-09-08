n = int(input('Insira um número natural: '))
if n <= 0:
    print('Número inválido: ')
else:
    soma = 0
    for i in range(1, n + 1):
        soma += i
    print(soma)
