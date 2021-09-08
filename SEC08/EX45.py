vetor = list(range(1, 46))

def desv_padr(vet):
    med = sum(vet) / len(vet)
    des = [(i - med) ** 2 for i in vet]
    return sum(des)

print(desv_padr(vetor))
