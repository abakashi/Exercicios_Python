import math

num = int(input('Insira um número inteiro positivo: '))
if num > 0:
    print(math.log10(num))
else:
    print('Numero negativo.')
