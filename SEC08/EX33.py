def soma_algarismos(n):
    from math import factorial
    fat = str(factorial(n))
    v_fat = [int(i) for i in fat]
    return sum(v_fat)

print(soma_algarismos(10))
