def randlista(lista):
    from random import randrange
    s_list = set(lista)
    s_list.clear()
    while len(s_list) != len(lista):
        s_list.add(randrange(999))
    r_list = list(s_list)
    r_list.sort()
    return r_list


siribi = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(randlista(siribi))