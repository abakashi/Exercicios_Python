bg = int(input('Insira a base maior: '))
bp = int(input('Insira a base menor: '))
if bg <= 0 or bp <= 0:
    print('As bases devem ser maiores do que zero!')
else:
    altura = int(input('Insira a altura: '))
    quo = (bg + bp) * altura
    area = quo / 2
    print(f'A Area do trapézio é: {area}.')
