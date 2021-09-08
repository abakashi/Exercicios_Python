b = int(input('Insira o valor da base: '))
h = int(input('Insira o valor da altura: '))
if b <= 0 or h <= 0:
    print('Os valores não pordem ser menores ou iguais a zero.')
else:
    area = (b * h) / 2
    print(area)
