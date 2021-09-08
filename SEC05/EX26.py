dist = float(input('Insira a distância em KM: '))
lit = float(input('Insira a quantidade de litros consumidos: '))

cons = dist / lit
if cons < 8:
    print(f'{cons:.2f} Km/l - Venda o carro!')
elif cons >=8 and cons <= 12:
    print(f'{cons:.2f} Km/l - Econômico!')
elif cons > 12:
    print(f'{cons:.2f} Km/l - Super econômico!')
