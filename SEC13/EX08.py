from formulas import trocaletra as toupper

with open('EX08in.txt', 'w') as escrita:
    entrada = input('Digite um texto: ')
    escrita.write(entrada)

with open('EX08in.txt', 'r') as leitura:
    print(toupper(leitura.read()))

