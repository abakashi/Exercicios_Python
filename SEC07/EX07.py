vetor = []
for i in range(10):
    entrada =  int(input(f'Insira a posição {i}: '))
    vetor.append(entrada)
print(vetor)
print(max(vetor))
print(vetor.index(max(vetor)))
