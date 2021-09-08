a = int(input('Insira um valor inteiro para o primeiro lado: '))
b = int(input('Insira um valor inteiro para o segundo lado: '))
c = int(input('Insira um valor inteiro para o terceiro lado: '))

if a + b < c or a + c < b or c + b < a:
    print('É impossível traçar um triângulo com estas medidas de lado.')
else:
    if a == b == c:
        print('Trângulo equilátero.')
    elif a == b or a == c or b == c:
        print('Triângulo isósceles.')
    elif a != b != c:
        print('Triângulo Escaleno.')
