num = int(input('Insira um número ímpar positivo: '))
if num % 2 == 0 and num <= 0:
    print('Número inválido.')
else:
    for i in range(1, num+1, 2):
        print(i)
