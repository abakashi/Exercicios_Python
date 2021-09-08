n = int(input('Insira um número natural: '))
if n <= 0:
    print('Número inválido.')
else:
    res = 0
    while res == 0:
        n += 1
        if n % 11 == 0 or n % 13 == 0 or n % 17 == 0:
            res = n
print(res)
