import random
n = int(input('Insira o número de vezes que os dados serão rolados: '))
for i in range(n):
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    if dado1 > dado2:
        print(f'{dado1} > {dado2}')
    elif dado2 > dado1:
        print(f'{dado2} > {dado1}')
    elif dado1 == dado2:
        print(f'{dado1} = {dado2}')
