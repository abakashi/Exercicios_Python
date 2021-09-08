cont = 1
cod = 0
valor = []
while cont == 1:
    cod = int(input('Insira o código do produto: \n'
                    '100 - Cachorro quente; \n'
                    '101 - Bauru simples;\n'
                    '102 - Bauru com ovo; \n'
                    '103 - Hamburguer;\n'
                    '104 - Cheeseburguer;\n'
                    '105 - Suco; \n'
                    '106 - Refrigerante;\n'))
    if cod == 100:
        valor.append(1.20)
    elif cod == 101:
        valor.append(1.30)
    elif cod == 102:
        valor.append(1.50)
    elif cod == 103:
        valor.append(1.20)
    elif cod == 104:
        valor.append(1.70)
    elif cod == 105:
        valor.append(2.20)
    elif cod == 106:
        valor.append(1.00)
    else:
        print('Código inválido')
    cont = int(input('Continuar? 1 - sim / 0 - não.'))
tot = sum(valor)
print(f'Total do pedido: R$: {tot:.2f}.')
