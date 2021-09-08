import datetime as dt

entrada = input('Insira a hora de entrada: ')
saida = input('Insira a hora de saída: ')

ent1 = int(dt.datetime.strptime(entrada, '%H:%M').strftime("%M"))
sai1 = int(dt.datetime.strptime(saida, '%H:%M').strftime("%M"))

ent2 = int(dt.datetime.strptime(entrada, '%H:%M').strftime("%H"))
sai2 = int(dt.datetime.strptime(saida, '%H:%M').strftime("%H"))

dif = (sai2 - ent2) * 60 + (ent1 - sai1)
#print(dif)

if dif <= 120:
    preco = (dif / 60) * 1
elif dif > 120 and dif <= 240:
    preco = (dif /60) * 1.4
elif dif > 240:
    preco = (dif / 60) * 2

print(f'O valor da estadia é R$: {preco:.2f}.\n'
      f'O tempo da estadia foi de {dif} minutos.')
