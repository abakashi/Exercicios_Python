valores = []
impares = []
entrada = 0
for i in range(10):
    entrada = int(input(f'Insira o {i + 1}º número: '))
    if entrada < 0 or entrada > 50:
        while entrada < 0 or entrada > 50:
            entrada = int(input(f'O número deve ser maior ou igual a 0 e menor que 51.\n'
                                f'Insira o {i + 1}º número: '))
    else:
        valores.append(entrada)
        if entrada % 2 != 0:
            impares.append(entrada)

for j in range(0, len(valores), 2):
    print(valores.__getitem__(j), valores.__getitem__(j + 1))
print('\n')

if len(impares) > 0 and len(impares) % 2 == 0:
    for k in range(0, len(impares), 2):
        print(impares.__getitem__(k), impares.__getitem__(k + 1))
else:
    for k in range(0, len(impares) + 1, 2):
        print(impares.__getitem__(k), impares.__getitem__(k + 1))
