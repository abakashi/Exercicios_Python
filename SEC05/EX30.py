numeros = []
for i in range(3):
    num = int(input(f'Insira o {i + 1}ͦ número: '))
    numeros.append(num)

numeros.sort()

for j in numeros:
    print(j, end=', ')
