a = int(input('Insira o número A: '))
b = int(input('Insira o número B: '))
while a >= 10000 or b >= 10000:
    print('Os números devem ter apenas 4 dígitos no máximo.')
    a = int(input('Insira o número A: '))
    b = int(input('Insira o número B: '))
a_s = str(a)
b_s = str(b)
va = []
n_a = ''
for i in range(len(a_s)):
    a_int = int(a_s[i])
    va.append(a_int)
print(va)
print('\n')
for i in range(len(va)):
    alg = str(va[i])
    n_a = n_a + alg
print(int(n_a) + b)
