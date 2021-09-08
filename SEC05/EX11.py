num = int(input('Insira um número: '))
if num > 0:
    lista = list(str(num))
    soma = []
    for i in range(len(lista)):
        soma.append(int(lista[i]))
    print(sum(soma))
else:
    print('Número inválido.')
