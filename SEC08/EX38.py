def fat_exp(n):
    fat = n
    for i in range(n - 1, 0, -1):
        fat = fat ** i
    return fat
