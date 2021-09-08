def ver_pos(num):
    if num > 0:
        return 1
    elif num < 0:
        return  -1
    elif num == 0:
        return 0

entrada = int(input('Bota um numu aí, ma: '))
print(ver_pos(entrada))