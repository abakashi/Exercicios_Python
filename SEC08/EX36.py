def sf(n):
    fat = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            fat = fat * j
    return fat

print(sf(5))