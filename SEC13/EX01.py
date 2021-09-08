with open('arq.txt', 'w') as arquivo:
    loop = True
    while loop:
        entrada = input('Insira uma informação (digite 0 para sair): ')
        if entrada == '0':
            loop = False
        else:
            arquivo.write(entrada)
            arquivo.write('\n')
print('\n', end=None)
with open('arq.txt', 'r') as file:
    print(file.read())