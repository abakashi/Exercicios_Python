num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))
pares = []
impares = []
if num1 > num2:
    print('Os primeiro número deve ser sempre o menor.')
else:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            pares.append(i)
        if i % 2 != 0:
            impares.append(i)
    print(f'Soma dos pares {sum(pares)}.\n'
          f'Soma dos ímpares {sum(impares)}.')
