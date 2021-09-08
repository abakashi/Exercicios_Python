def media(*args, tipo='a'):
    if tipo.lower() == 'a':
        m = sum(args) / len(args)
        return m
    else:
        p = (5, 3, 2)
        mult = []
        for i in range(len(p)):
            n = args[i] * p[i]
            mult.append(n)
        if len(args) > 3:
            for i in range(3, len(args)):
                mult.append(args[i])
        m = sum(mult) / len(mult)
        return m

cont = 0

print(media(1, 3, 5, 7, tipo='a'))

