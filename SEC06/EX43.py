notas = []
while True:
    n = float(input('Insira uma nota: '))
    if n <= 0:
        med = sum(notas) / len(notas)
        print(med)
        break
    notas.append(n)
