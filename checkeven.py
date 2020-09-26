# def check(a):
#     if a % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
#
# b = int(input("Enter Number: "))
# check(b)


x = int(input("Enter Starting: "))
y = int(input("Enter Ending: "))
for a in range(x, y):
    if a % 2 == 0:
        print(a, "Even")
    else:
        print(a, "Odd")
