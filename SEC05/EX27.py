idade = int(input('Insira a idade do nadador: '))
if idade >= 5 and idade <= 7:
    print('Nadador na categoria Infantil A.')
elif idade >= 8 and idade <= 10:
    print('Nadador na categoria Infantil B.')
elif idade >= 11 and idade <= 13:
    print('Nadador na categoria Juvenil A.')
elif idade >= 14 and idade <= 17:
    print('Nadador na categoria Juvenil B.')
elif idade >= 18:
    print('Nadador na categoria Senior.')
else:
    print('Nadador não pôde ser classificado.')
