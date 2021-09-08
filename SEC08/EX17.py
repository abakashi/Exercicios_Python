def soma_num(num1, num2):
    listanum = [numero for numero in range(num1+1,num2)]
    return sum(listanum)

print(soma_num(20, 30))