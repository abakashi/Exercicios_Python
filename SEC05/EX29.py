from random import randint
pontos = 0
for i in range(5):
    a = randint(1, 101)
    b = randint(1, 101)
    resp = int(input(f'Quanto é {a} + {b}?\n'))
    if resp == a + b:
        print(f'Parabéns! Você acertou!\nA resposta é {a + b}!\n')
        pontos = pontos + 1
    else:
        print(f'Que pena, você disse {resp}.\nA resposta correta seria {a + b}.\n')
print(f'Você acertou {pontos} perguntas.')
