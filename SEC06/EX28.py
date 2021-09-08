import math
vetor = []
n = int(input('Insira um valor inteiro e positivo: '))
if n <= 0:
    print('Número inválido.')
else:
    for i in range (1, n + 1):
        vetor.append(1 / math.factorial(i))
    e = sum(vetor) + 1
    print(e)
