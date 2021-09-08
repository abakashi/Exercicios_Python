def imp_norm(vet):
    return print(vet)

def imp_inv(vet):
    vet.reverse()
    return print(vet)

def media(vet):
    med = sum(vet) / len(vet)
    return print(med)

lol = list(range(1, 21))

imp_norm(lol)

imp_inv(lol)

media(lol)
