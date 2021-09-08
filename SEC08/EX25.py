def calc_01(n):
    soma = []
    for i in range(1, n + 1):
        num = (i ** 2 + 1) / (i + 3)
        soma.append(num)
    return sum(soma)

print(calc_01(10))