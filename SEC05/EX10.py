sexo = input('Insira seu sexo (m/f): ')
if sexo.lower() != 'm' and sexo.lower() != 'f':
    print('Sexo inválido.')
else:
    alt = float(input('Insira a sua altura: '))
    if sexo.lower() == 'm':
        p_ideal = (72.7 * alt) - 58
        print(f'Seu peso ideal como homem é {p_ideal:.2f}.')
    elif sexo.lower() == 'f':
        p_ideal = (62.1 * alt) - 44.7
        print(f'Seu peso ideal como mulher é {p_ideal:.2f}.')
