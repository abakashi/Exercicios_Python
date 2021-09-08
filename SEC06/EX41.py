while True:
    r1 = float(input('Insira O valor do primeiro resistor: '))
    if r1 == 0:
        print('Finalizado.')
        break
    r2 = float(input('Insira O valor do segundo resistor: '))
    if r2 == 0:
        print('Finalizado.')
        break
    resis = ( r1 * r2 ) / ( r1 + r2 )
    print(resis)

