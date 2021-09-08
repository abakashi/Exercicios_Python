with open('ex06.txt', 'w') as escrita:
    entrada = input('Insira um texto: ')
    escrita.write(entrada)

alfabeto = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z')

ocorrencias = {}

with open('ex06.txt', 'r') as leitura:
    saida = leitura.read().lower()
    for letra in alfabeto:
        if letra in saida:
            contagem = saida.count(letra)
            ocorrencias[letra] = contagem

for letra, ocorrencia in ocorrencias.items():
    print(f'A letra "{letra.upper()}" aparece {ocorrencia} vez(es).', end='\n')
