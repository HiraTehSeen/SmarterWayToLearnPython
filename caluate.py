# num_1 = int(input())
# op = input()
# num_2 = int(input())
var = [int(input()), input(), int(input())]
x = ['+', '-', '*', '/', '=']

for i in x:
    def check():
        if var[1] == '=':
            return 0
        else:
            var[2] = int(input())
            return var[2]

    if var[1] == '+':
        var[0] = var[0] + var[2]
        print(var[0])
    elif var[1] == '-':
        var[0] = var[0] - var[2]
        print(var[0])
    elif var[1] == '*':
        var[0] = var[0] * var[2]
        print(var[0])
    elif var[1] == '/':
        var[0] = var[0] / var[2]
        print(var[0])
    else:
        break

    var[1] = input()
    var[2] = check()

print(var[0])

