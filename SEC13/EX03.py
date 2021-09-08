""""
nome = 'Marco Antonio da Silva Cruz'
vogais = 0
consoantes = 0
vogais_tp = ('a', 'e', 'i', 'o', 'u')
for letra in nome:
    if letra.lower() in vogais_tp:
        vogais += 1
    elif letra.lower() not in vogais_tp and letra.lower() != ' ':
        consoantes += 1
print(vogais, consoantes, sep='\n')
"""
with open('texto.txt', 'r') as arquivo:
    vog = 0
    cons = 0
    vog_tp = ('a', 'e', 'i', 'o', 'u')
    for letra in arquivo.read():
        if letra.lower() in vog_tp:
            vog += 1
        elif letra.lower() not in vog_tp and letra.lower() != ' ':
            cons += 1
    print(f'Vogais: {vog}', f'COnsoantes {cons}', sep='\n')
