maior = -999
menor = 999
while True:
    num = int(input('Insira um número: '))
    if num < 0:
        break
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(menor)
print(maior)
