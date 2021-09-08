num = int(input('Insira um número par inteiro positivo: '))
if num % 2 != 0 and num <= 0:
    print('Número inválido.')
else:
    for i in range(num, -1, -2):
        print(i)
