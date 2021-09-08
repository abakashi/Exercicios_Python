cata = float(input('Insira o valor do primeiro cateto: '))
catb = float(input('Insira o valor do segundo cateto: '))
hipotenusa = (cata ** 2 + catb ** 2) ** 0.5
area = ( cata * catb ) / 2
print(f'{hipotenusa:.2f} é a hupotenusa. \n{area:.2f} é a área.')
