print('Escolha uma opção:\n'
      '1 - Soma de dois números;\n'
      '2 - Diferença entre 2 números (maior pelo menor);\n'
      '3 - Produto entre dois números;\n'
      '4 - Divisão entre dois números.\n')
op = int(input('Digite a opção: '))
if op <= 0 or op >= 5:
    print('Opção inválida.')
else:
    if op == 1:
        soma = []
        for i in range(2):
            num = float(input(f'Insira o {i+1}ͦ valor: '))
            soma.append(num)
        print(f'O valor da soma é {sum(soma)}.')
    elif op == 2:
        num1 = float(input('Insira o maior número: '))
        num2 = float(input('Insira o menos número: '))
        while num1 < num2:
            print('O primeiro número deve ser o maior.')
            num1 = float(input('Insira o maior número: '))
            num2 = float(input('Insira o menos número: '))
        sub = num1 - num2
        print(sub)
    elif op == 3:
        num1 = float(input('Insira um número: '))
        num2 = float(input('Insira outro número: '))
        mult = num1 * num2
        print(mult)
    elif op == 4:
        num1 = float(input('Insira numerador: '))
        num2 = float(input('Insira o denominador: '))
        while num2 == 0:
            num2 = float(input('O denominador deve ser diferente de zero.\nInsira o novo denominador: '))
        div = num1 / num2
        print(div)
