v1 = []
v2 = []
for i in range(5):
    v1.append(int(input(f'Insira o {i + 1} número do primero vetor: ')))
    v2.append(int(input(f'Insira o {i + 1} número do segundo vetor: ')))
for i in range(len(v1)):
    print(f'A soma dos números de índice {i} é {v1[i] + v2[i]}.')
for i in range(len(v1)):
    print(f'O produto dos números de índice {i} é {v1[i] * v2[i]}.')
for i in range(len(v1)):
    print(f'A diferença dos números de índice {i} é {v1[i] - v2[i]}.')
s1 = set(v1)
s2 = set(v2)

print(f'A intersecção entre os dois vetores é {s1.intersection(s2)}.')
print(f'A união entre os dois vetores é {s1.union(s2)}.')

