menor = 999
maior = -999
for _ in range(10):
    num = int(input('Insira um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(menor)
print(maior)
