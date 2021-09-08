def hfat(n):
    fat = 1
    for i in range(1, n + 1):
        fat = fat * (i ** i)
    return fat

print(hfat(4))
