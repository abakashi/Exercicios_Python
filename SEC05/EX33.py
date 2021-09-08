nota = float(input('Insira a nota do aluno: '))
falta = int(input('Insira o número de faltas: '))

if nota >= 9.0 and nota <= 10:
    if falta <= 20:
        print('Conceito A')
    elif falta > 20:
        print('Conceito B')
elif nota >= 7.5 and nota <= 8.9:
    if falta <= 20:
        print('Conceito B')
    elif falta > 20:
        print('Conceito C')
elif nota >= 5.0 and nota <= 7.4:
    if falta <= 20:
        print('Conceito C')
    elif falta > 20:
        print('Conceito D')
elif nota >= 4.0 and nota <= 4.9:
    if falta <= 20:
        print('Conceito D')
    elif falta > 20:
        print('Conceito E')
elif nota >= 0.0 and nota <= 3.9:
    if falta <= 20:
        print('Conceito E')
    elif falta > 20:
        print('Conceito E')
else:
    print('Nota inválida.')
