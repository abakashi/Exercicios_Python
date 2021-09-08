def fator_primo(num):
    primos = []
    fatores = []
    for i in range(1, num+1):
        div = []
        for j in range(1, i):
            if i % j == 0:
                div.append(j)
        if len(div) < 2:
            primos.append(i)
        div.clear()
    for k in primos:
        if num % k == 0:
            fatores.append(k)
    fatores.reverse()
    return fatores[0]



print(fator_primo(49))
