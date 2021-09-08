notas = []
contador = 0
num = 10
while num >= 10 and num <= 20:
    num = float(input(f'Insira a nota da {contador + 1}ª prova: '))
    if num >= 10 and num <= 20:
        contador += 1
        notas.append(num)
med = sum(notas) / contador
print(f'A quantidade de provas foi {contador}.\n'
      f'A média final de todas as notas foi {med:.2f}.')
