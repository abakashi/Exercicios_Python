c_fabrica = float(input('Insira o custo de fábrica do carro: '))
if c_fabrica <= 12_000:
    c_consu = c_fabrica + (c_fabrica * 0.05)
    print(c_consu)
elif c_fabrica > 12_000 and c_fabrica <= 25_000:
    c_consu = c_fabrica + (c_fabrica * 0.1) + (c_fabrica * 0.15)
    print(c_consu)
elif c_fabrica > 25_000:
    c_consu = c_fabrica + (c_fabrica * 0.15) + (c_fabrica * 0.20)
    print(c_consu)
