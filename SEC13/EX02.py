with open('texto.txt', 'w') as arquivo:
    loop = True
    while loop:
        entrada = str(input('Insira uma linha do texto (digite SAIR para fechar): '))
        if entrada.lower() == 'sair':
            loop = False
        else:
            arquivo.write(entrada)
            arquivo.write('\n')

with open('texto.txt', 'r') as file:
    lista_linhas = list(file.read().split('\n'))
    print(f'Você digitou {len(lista_linhas) - 1} linhas.')
