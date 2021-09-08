soma_quad = []
soma = []
for i in range(1, 101):
    quad_1 = i ** 2
    soma_quad.append(quad_1)
print(soma_quad)
for j in range(1, 101):
    soma.append(j)
print(soma)

dif = (sum(soma) ** 2) - sum(soma_quad)
print(dif)
