res = []
for i in range(1000, 10000):
    str_i = str(i)
    n1 = int(str_i[0:2])
    n2 = int(str_i[2:4])
    calc = n1 + n2
    if calc ** 2 == i:
        res.append(i)
print(res)
