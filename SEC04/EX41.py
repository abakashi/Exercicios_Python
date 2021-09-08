valor = float(input('Insira o valor por hora trabalhada: '))
horas = float(input('Insira a quantidade de horas trabalhadas: '))
sal = (valor * horas) * 1.1
print(f'Valor a ser pago ao funcionário R$: {sal:.2f}.')
