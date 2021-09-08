
def ddata(dia, mes, ano):
    meses = ( 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro' )
    return f'{dia}, de {meses[mes-1]} de {ano}'


cont = 's'
while cont.lower() == 's':
    dia = int(input('Insira o dia: '))
    mes = int(input('Insira o mês: '))
    ano = int(input('Insira o ano: '))
    print(ddata(dia, mes, ano))
    cont = input('continuar? ')

