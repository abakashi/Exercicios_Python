vetor = []
while True:
    num = int(input('Insira um número postivo: '))
    if num <= 0:
        for i in vetor:
            print(i ** 2, end=', ')
        print('\n')
        for j in vetor:
            print(j ** 3, end=', ')
        print('\n')
        for k in vetor:
            print(k ** 0.5, end=', ')
        break
    vetor.append(num)
