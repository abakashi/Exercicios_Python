a = []
b = []
for i in range(10):
    a.append(int(input(f'Insira o {i + 1}º número para o vetor A: ')))
    b.append(int(input(f'Insira o {i + 1}º número para o vetor B: ')))
c = []
for j in range(len(a)):
    c.append(a[j] - b[j])
print(c)
