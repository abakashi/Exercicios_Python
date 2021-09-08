def fat_duplo(num):
    multi = 1
    for i in range(1, num + 1):
        if i % 2 != 0:
            multi = multi * i
    return multi

