vetor1 = []
vetor2 = []
for i in range(10):
    vetor1.append(int(input(f'Insira o valor {i + 1} do primeiro vetor: ')))
for j in range(10):
    vetor2.append(int(input(f'Insira o valor {j + 1} do segundo vetor: ')))
sv1 = set(vetor1)
sv2 = set(vetor2)

inter = sv1.intersection(sv2)
print(inter)
