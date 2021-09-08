notas = []
pesos = [2, 3, 5]
soma = []
lab = float(input('Insira a nota do Laboratório: '))
notas.append(lab)
avasem = float(input('Insira a nota da Avaliação Semestral: '))
notas.append(avasem)
exfin = float(input('Insira a nota do Exame Final: '))
notas.append(exfin)
for i in range(3):
    soma.append(notas[i] * pesos[i])
media = sum(soma) / sum(pesos)
if media >= 0 and media <= 2.9:
    print(f'Média {media:.2f}, aluno reprovado.')
elif media >= 3 and media <= 4.9:
    print(f'Média {media:.2f}, aluno em recuperação.')
else:
    print(f'Média {media:.2f}, aluno aprovado.')
