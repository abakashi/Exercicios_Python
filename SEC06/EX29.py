import math
vetor = []
for i in range(1, 6):
    vetor.append(i / math.factorial(i * 2))
s = sum(vetor)
print(s)
