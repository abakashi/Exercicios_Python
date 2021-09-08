hora = int(input('Insira a hora: '))
min = int(input('Insira os minutos: '))
seg = int(input('Insira os segundos: '))
duracao = int(input('Insira a duração em segundos: '))

seg_f = seg + duracao
min_f = (seg_f / 60) + min
hor_f = (min_f / 60) + hora

print(hor_f)
print(min_f)
print(seg_f)
