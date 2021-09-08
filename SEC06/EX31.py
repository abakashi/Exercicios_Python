vetor = []
for i in range(1, 51):
    num = 2 * i - 1
    vetor.append(num / i)
s = sum(vetor)
print(s)
