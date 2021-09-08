cnt = 0
while cnt == 0:
    print('Calculadora de Raízes de equação do segundo grau\n ax²+bx+c')
    a = int(input('Insira o valor de a: '))
    if a == 0:
        print('a deverá sempre ser diferente de 0.')
        cnt = int(input('Reiniciar? (0 - sim; 1 - não)\n'))
    else:
        b = int(input('Insira o valor de b: '))
        c = int(input('Insira o valor de C: '))
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            print('Não existe raiz real.')
            cnt = int(input('Reiniciar? (0 - sim; 1 - não)\n'))
        elif delta > 0:
            x1 = (-1 * b + delta ** 0.5) / 2 * a
            x2 = (-1 * b - delta ** 0.5) / 2 * a
            print(f'Os valores das raízes são: {x1} e {x2}.')
            cnt = int(input('Reiniciar? (0 - sim; 1 - não)\n'))
        elif delta == 0:
            x3 = (-1 * b) / 2 * a
            print(f'A equação tem uma única raiz: {x3}.')
            cnt = int(input('Reiniciar? (0 - sim; 1 - não)\n'))
