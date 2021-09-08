def vol_esfera(raio):
    v = (4/3) * 3.1415 * (raio ** 3)
    return v

while True:
    entrada = input('Insira o raio da esfera, digite "X" para sair: ')
    if entrada.lower() == 'x':
        break
    else:
        print(vol_esfera(float(entrada)))