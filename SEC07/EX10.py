notas = []
for i in range(15):
    entrada = float(input(f'Insira a nota do {i+1}º aluno:'))
    notas.append(entrada)
med = sum(notas) / len(notas)
print(f'{med:.2f}')
