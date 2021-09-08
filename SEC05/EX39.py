sal = float(input('Insira o valor do salário do funcionário: '))
tem_serv = int(input('Tempo de serviço em anos: '))
reaj = 0

if sal <= 500:
    reaj1 = sal + (sal * 0.25)
    print(f'Salário reajustado R$: {reaj1:.2f}.')
elif sal > 500 and sal <= 1000:
    reaj1 = sal + (sal * 0.20)
    if tem_serv >= 1 and tem_serv <= 3:
        reaj = reaj1 + 100
        print(f'Salário reajustado R$: {reaj:.2f}.')
    else:
        print(f'Salário reajustado R$: {reaj1:.2f}.')
elif sal > 1000 and sal <= 1500:
    reaj1 = sal + (sal * 0.15)
    if tem_serv >= 4 and tem_serv <= 6:
        reaj = reaj1 + 200
        print(f'Salário reajustado R$: {reaj:.2f}.')
    else:
        print(f'Salário reajustado R$: {reaj1:.2f}.')
elif sal > 1500 and sal <= 2000:
    reaj1 = sal + (sal * 0.1)
    if tem_serv >= 7 and tem_serv <= 10:
        reaj = reaj1 + 300
        print(f'Salário reajustado R$: {reaj:.2f}.')
    else:
        print(f'Salário reajustado R$: {reaj1:.2f}.')
elif sal > 2000:
    if tem_serv > 10:
        reaj = sal + 500
        print(f'Salário reajustado R$: {reaj:.2f}.')
    else:
        print(f'Sem reajuste.')
