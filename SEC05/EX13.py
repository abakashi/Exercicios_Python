notas = []
pesos = [1, 2, 3]
soma = 0
for i in range(3):
    num = float(input(f'Insira a {i+1} nota: '))
    notas.append(num)
for j in range(3):
    n = notas[j] * pesos[j]
    soma = soma + n
media = soma / sum(pesos)
print(f'{media:.2f}')
