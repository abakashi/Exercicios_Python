def quant_primos(num):
    primos = []
    for i in range(1, num+1):
        div = []
        for j in range(1, i):
            if i % j == 0:
                div.append(j)
        if len(div) < 2:
            primos.append(i)
        div.clear()
    return len(primos)

print(quant_primos(7))