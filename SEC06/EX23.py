num = int(input('Insira um número positivo: '))
if num <= 0:
    print('Número inválido.')
else:
    for i in range (1, num + 1):
        if num % i == 0:
            print(i)
