numeros = []
multiplos = []

for i in range(10):
    numeros.append(int(input(f'Insira o {i+1}º número: ')))

mult = int(input('Insira o número para o qual você quer fazer a operação: '))

for i in range(len(numeros)):
    if numeros[i] % mult == 0:
        multiplos.append(numeros[i])
print(numeros)
print(multiplos)
