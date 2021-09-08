soma = 0
cont = 0
for i in range (10):
    num = int(input('Insira um número inteiro:'))
    if num > 0:
        soma += num
        cont += 1
med = soma / cont
print(med)
