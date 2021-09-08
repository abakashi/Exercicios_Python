valores = []
for i in range(10):
    entrada = int(input(f'Insira o {i + 1} número: '))
    if entrada in valores:
        while entrada in valores:
            entrada = int(input(f'Você não pode adicionar um número já usado.\n'
                                f'Insira o {i + 1} número: '))
        else:
            valores.append(entrada)
    else:
        valores.append(entrada)
print(valores)
