numero = int(input('Insira um numero de 4 digitos: '))
if numero >= 1000 and numero <=9999:
    st_num = str(numero)
    for i in range(0, 4):
        print(st_num[i])
else:
    print('O número deve ter obrigatoriamente 4 dígitos.')
