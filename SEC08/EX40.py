def num_pares(vet):
    vpar = [i for i in vet if i % 2 == 0]
    return len(vpar)

boga = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num_pares(boga))
