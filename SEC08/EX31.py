def num_neper(n):
    from math import factorial
    l = [1 / factorial(i) for i in range(n + 1)]
    return sum(l)

print(num_neper(30))