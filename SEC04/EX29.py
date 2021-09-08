soma = 0
for i in range(1, 5):
    nota = float(input(f'Insira a {i}ª nota: '))
    soma = soma + nota
media = float(soma / 4)
print(f'Média das notas é: {media:.2f}.')
