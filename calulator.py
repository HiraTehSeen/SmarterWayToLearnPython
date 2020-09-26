def cal(a, o, b):
    if o == '+':
        c = a + b
        return c
    elif o == '-':
        c = a - b
        return c
    elif o == '*':
        c = a * b
        return c
    elif o == '/':
        c = a / b
        return c
    else:
        print("Wrong Operator")
        return 0


num1 = int(input("Enter Number: "))
op = input("Enter Operator: ")
num2 = int(input("Enter Number: "))
res = cal(num1, op, num2)
print(res)

