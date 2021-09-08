a = []
b = []
pescalar = []
for i in range(5):
    a.append(float(input(f'Insira o {i + 1}º número do grupo A: ')))
    b.append(float(input(f'Insira o {i + 1}º número do grupo b: ')))
for i in range(len(a)):
    pescalar.append(a[i] * b[i])

produto = sum(pescalar)
print(produto)
