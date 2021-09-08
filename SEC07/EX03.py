vetor = []
quad_vet = []
for i in range(10):
    entrada = float(input('Insira um número: '))
    vetor.append(entrada)
for j in range(len(vetor)):
    quad = vetor[j] ** 2
    quad_vet.append(quad)
print(vetor)
print(quad_vet)
