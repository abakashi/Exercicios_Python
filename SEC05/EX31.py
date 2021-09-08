alt = float(input('Insira a sua altura: '))
peso = int(input('Insira o seu peso: '))

if alt < 1.20:
    if peso <= 60:
        print('Classificação A')
    elif peso > 60 and peso <= 90:
        print('Classificação D')
    elif peso > 90:
        print('Classificação G')
elif alt >= 1.20 and alt <= 1.70:
    if peso <= 60:
        print('Classificação B')
    elif peso > 60 and peso <= 90:
        print('Classificação E')
    elif peso > 90:
        print('Classificação H')
elif alt > 1.70:
    if peso <= 60:
        print('Classificação C')
    elif peso > 60 and peso <= 90:
        print('Classificação F')
    elif peso > 90:
        print('Classificação I')
