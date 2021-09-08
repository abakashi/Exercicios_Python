valores = []
for i in range(10):
    valores.append(float(input(f'Insira o {i+1} número: ')))
med = sum(valores) / len(valores)
sd = []

for i in range(len(valores)):
    dmed = (valores[i] - med) ** 2 / len(valores)
    sd.append(dmed)
dp = (sum(sd)) ** 0.5
print(dp)
