notas = []
print()
while True:
    print('Para sair digite um número negativo ou acima de 10.')
    nota = float(input(f'Insira uma nota válida (entre 0 e 10)\n {len(notas)} nota(s) inserida(s): '))
    if float(nota) >= 0 and nota <= 10:
        notas.append(float(nota))
    else:
        break

med = sum(notas) / len(notas)
print(f'{med:.2f} é a média final.')
print(notas)
