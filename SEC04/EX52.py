premio = float(input('Insira o valor do prêmio: '))
aposta = []
soma = 0
for i in range(0, 3):
    num = float(input(f'Insira o valor da aposta do {i + 1}º amigo: '))
    aposta.append(num)
    soma = soma + num
for j in range(0, 3):
    ind_prop = aposta[j] / soma
    pre_prop = premio * ind_prop
    print(f'O amigo {j + 1} vai receber: R$: {pre_prop:.2f}.')
