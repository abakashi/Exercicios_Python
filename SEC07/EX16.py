numeros = []

for i in range(5):
    numeros.append(float(input(f'Insira o {i+1}º número: ')))

cod = int(input(f'Insira o código:\n'
                f'1 - Ordem direta;\n'
                f'2 - Ordem Inversa:\n'))
if cod != 1 or cod != 2:
    while cod != 1 and cod != 2:
        print('O valor deve ser obrigatoriamente 1 ou 2.')
        cod = int(input(f'Insira o código:\n'
                    f'1 - Ordem direta;\n'
                    f'2 - Ordem Inversa:\n'))
if cod == 1:
    print(numeros)
if cod == 2:
    numeros.reverse()
    print(numeros)
