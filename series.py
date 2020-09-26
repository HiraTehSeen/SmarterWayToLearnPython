# series of number
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print("\r")
# Example of series of number
for item in range(1, 6):
    a = ''
    for data in range(0, item):
        a += str(item)
    print(a)

# reverse string
s = input("Enter String: ")
sp = ""
for i in s:
    sp = i + sp
print(sp)


# reverse string using function
def rev(string):
    space = ""
    for x in string:
        space = x + space
    return space


ch = input("Enter String: ")
print(rev(ch))
