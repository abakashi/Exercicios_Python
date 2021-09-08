def oper_arit(num1, num2, op):
    if op == '-':
        return num1 - num2
    elif op == '+':
        return  num1 + num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2


print(oper_arit(45, 30, '*'))