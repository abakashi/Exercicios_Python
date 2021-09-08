import math
x = int(input('Insira o primeiro número: '))
y = int(input('Insira o segundo número: '))
z = int(input('Insira o terceiro número: '))

op = int(input('Insira uma opção:\n'
               '1 - Média geométrica;\n'
               '2 - Média ponderada;\n'
               '3 - Média harmônica;\n'
               '4 - Média aritimética.\n'))
if op == 1:
    multi = x * y * z
    medg = math.pow(multi, 1/3)
    print(medg)
elif op == 2:
    medpon = (x + 2 * y + 3 * z) / 6
    print(medpon)
elif op == 3:
    som = (1 / x) + (1 / y) + (1 / z)
    medharm = 1 / som
    print(medharm)
elif op == 4:
    medari = (x + y + z) / 3
    print(medari)
else:
    print('Opção inválida.')
