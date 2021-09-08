soma = 0
n = int(input('Insira um número inteiro positivo: '))
if n <= 0:
    print('Número inválido: ')
else:
    for i in range(1, n + 1):
        soma += i
print(soma)
