lista = list(range(1, 31))

def par_impar(vet):
    a = [i for i in vet if i % 2 == 0]
    b = [j for j in vet if j % 2 != 0]
    return [a, b]

print(par_impar(lista))
