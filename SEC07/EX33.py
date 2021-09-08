marzelinho = []
for i in range(15):
    marzelinho.append(int(input(f'Insira um número para a posição {i}: ')))
for i in range(len(marzelinho)):
    if 0 in marzelinho:
        marzelinho.pop(marzelinho.index(0))
print(marzelinho)
