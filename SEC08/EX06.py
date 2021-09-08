def seg_conv(segundos, minutos=0, hora=0):
    s_hora = hora * 3600
    s_min = minutos * 60
    tot_seg = s_hora + s_min + segundos
    return tot_seg

hora = int(input('Insira a quantidade de horas: '))
minutos = int(input('Insira a quantidade de minutos: '))
segundos = int(input('Insira a quantidade de segundos: '))

print(seg_conv(segundos=segundos, minutos=minutos, hora=hora))