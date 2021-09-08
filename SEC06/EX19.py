num = int(input('Insira um número entre 100 e 999: '))
if num < 100 or num > 999:
    print('Número Inválido.')
else:
    num_str = str(num)
    for i in num_str:
        print(i)
