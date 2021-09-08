with open('ex07.txt', 'w') as escrita:
    entrada = input('Insira um texto: ')
    escrita.write(entrada)

vogais = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

nova_saida = ''
with open('ex07.txt', 'r') as leitura:
    saida = leitura.read()
    for letra in saida:
        if letra in vogais:
            nova_saida = nova_saida + '*'
        else:
            nova_saida = nova_saida + letra

with open('ex07_svogais.txt', 'w') as escrita:
    escrita.write(nova_saida)

with open('ex07_svogais.txt', 'r') as leitura:
    print(leitura.read())
