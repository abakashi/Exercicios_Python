seg = int(input('Insira o valor em segundos: '))
min = float(seg / 60)
hor = float(min / 60)

print(f'Em horas {hor:.3f}.\nEm minutos {min:.3f}.\nEm segundos {seg}.')
