#contador = 0
#maior = -99999
valor = []
q = int(input('Insira a quantidade de números: '))
if q <= 0:
    print('Quantidade inválida.')
else:
    for i in range(q):
        num = int(input(f'Insira o {i+1}º número: '))
        valor.append(num)
print(f'{max(valor)} é o maior valor.')
print(f'O valor aparece {valor.count(max(valor))} vezes.')
