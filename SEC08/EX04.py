def quad_perf(numero, ind=2):
    quad = []
    indice = 1 / ind
    raiz = int(numero ** indice)

    for i in range(1, raiz+1):
        qua = i ** 2
        quad.append(qua)
    if numero in quad:
        return 'É quadrado perfeito.'
    else:
        return 'Não é quadrado perfeito.'

while True:
    entrada = input('Insira um número, digite "X" para sair: ')
    if entrada.lower() == 'x':
        break
    else:
        print(quad_perf(int(entrada)))
