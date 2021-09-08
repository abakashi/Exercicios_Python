int1 = int(input('Insira o valor inicial do intervalo: '))
int2 = int(input('Insira o valor final do intervalo: '))
soma = 0
if int1 > int2:
    print('O valor inicial deve sempre ser o menor.')
else:
    for i in range(int1, int2 + 1):
        if i % 2 != 0:
            soma += i
    print(soma)
