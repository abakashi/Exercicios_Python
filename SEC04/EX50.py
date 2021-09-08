from datetime import date
ano = str(date.today())
ano[0:4]
idade = int(input('Insira a sua idade: '))
an_nasc = int(ano[0:4]) - idade
print(f'Você nasceu em {an_nasc}.')
