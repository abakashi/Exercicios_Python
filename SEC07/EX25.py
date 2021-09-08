vetor = []
for i in range(1, 101):
    if i % 7 == 0 or str(i)[-1] == '7':
        vetor.append(i)
print(vetor)
