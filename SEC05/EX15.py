dias = {1: 'Domingo', 2: 'Segunda', 3: 'Terça', 4: 'Quarta', 5: 'Quinta', 6: 'Sexta', 7: 'Sábado'}
num = int(input('Insira um número: '))
if num < 1 or num > 7:
    print('Número inválido.')
else:
    print(dias[num])
