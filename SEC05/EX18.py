num1 = float(input('Insira o primeiro número: '))
oper = input('Digite a operação que vc deseja: (+,-,/,*): ')
num2 = float(input('Insira o segundo número: '))
if oper == '+':
    print(num1 + num2)
elif oper == '-':
    print(num1 - num2)
elif oper == '/':
    print(num1 / num2)
elif oper == '*':
    print(num1 * num2)
else:
    print('Operação inválida.')
