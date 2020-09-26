def fac(a):
    f = 1
    for a in range(1, a+1):
        f *= a
    return f


i = int(input("Enter Number: "))
res = fac(i)
print(res)
