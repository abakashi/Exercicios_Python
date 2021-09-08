def simplifica(num, den):

    div_n = [i for i in range(1, num + 1) if num % i == 0]
    div_d = [j for j in range(1, den + 1) if den % j == 0]

    s_div_d = set(div_d)
    s_div_n = set(div_n)

    interc = s_div_d.intersection(s_div_n)
    l_interc = list(interc)
    l_interc.sort()
    l_interc.reverse()


    return str(int(num / l_interc[0]))+'/'+ str(int(den / l_interc[0]))

print(simplifica(27,81))


