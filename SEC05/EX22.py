id = int(input('Insira a sua idade: '))
ts = int(input('Insira o seu tempo de serviço: '))

if id >= 65 or ts >= 30:
    print('Elegível para aposentadoria.')
elif id >= 60 and ts >= 25:
    print('Elegível para aposentadoria.')
else:
    print('Não elegível para aposentadoria.')
