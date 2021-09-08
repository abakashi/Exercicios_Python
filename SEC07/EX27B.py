numeros = []
fatores = []
primos = []
for i in range(1000):
    numeros.append(i + 1)
for i in range(len(numeros)):
    ind = numeros[i]
    if ind != 1 and ind > 0:
        for j in range(1, ind + 1):
            if ind % j == 0:
                fatores.append(j)
        if len(fatores) <= 2:
            primos.append(ind)
    fatores.clear()

print(primos)
