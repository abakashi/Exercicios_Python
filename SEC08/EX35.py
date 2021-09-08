def fat_quad(n):
    fat = 1
    fat_2 = 1
    for i in range(1, n + 1):
        fat = fat * i
    for j in range(1, 2 * n + 1):
        fat_2 = fat_2 * j
    f_quad = int(fat_2 / fat)
    return  f_quad

print(fat_quad(5))
