def sinaizinhos(num):
    sinais = []
    for n in range(1, num+1):
        sinal = '!' * n
        sinais.append(sinal)
    return print(*sinais, sep='\n')

sinaizinhos(7)
