a = []
ap = []
apc = -1
b = []
bi = []
bic = -1
c = []
for i in range(10):
    enta = int(input(f'Insira o {i} um valor para A: '))
    a.append(enta)
    if enta % 2 == 0:
        apc += 1
        ap.append(enta)
    entb = int(input(f'Insira o {i} um valor para B: '))
    b.append(entb)
    if entb % 2 != 0:
        bic += 1
        bi.append(entb)
if apc > bic:
    while apc >= 0:
        if bic >= 0:
            c.append(bi[bic])
            bic -= 1
        c.append(ap[apc])
        apc -= 1

if apc < bic:
    while bic >= 0:
        c.append(bi[bic])
        bic -= 1
        if apc >= 0:
            c.append(ap[apc])
            apc -= 1

if apc == bic:
    while apc >= 0:
        c.append(bi[bic])
        bic -= 1
        c.append(ap[apc])
        apc -= 1

c.reverse()

print(a)
print(b)
print(c)
