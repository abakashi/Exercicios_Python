import random
num = random.randrange(1, 1000)
cont = 1
while True:
    inp = int(input('Insira um número: '))
    if inp == num :
        print(f'Acerou! O número é {num} em {cont} tentativas!')
        break
    elif inp < num:
        print(f'\nO número é maior que {inp}.\n')
        cont += 1
    elif inp > num:
        print(f'\nO número é menor que {inp}.\n')
        cont += 1
