def somalgarismos(numero):
    num = str(numero)
    soma = []
    for i in range(len(num)):
        numint = int(num[i])
        soma.append(numint)
    return sum(soma)

print(somalgarismos(3577))
