# table
table = int(input("Enter a Number: "))
for i in range(1, 11):
    res = table * i
    print(f"{table} x {i} = {res}")


# max and min number from list
num_list = []
for i in range(0, 3):
    a = int(input("Enter Numbers: "))
    num_list.append(a)

print(num_list)
num = 0
s = input("Enter max or min: ")
if s == "max":
    if num_list[0] > num_list[1]:
        num = num_list[0]
    else:
        num = num_list[1]
    if num > num_list[2]:
        print(f"Maximum Number in List: {num}")
    else:
        num = num_list[2]
        print(f"Maximum Number in List: {num}")
elif s == "min":
    if num_list[0] < num_list[1]:
        num = num_list[0]
    else:
        num = num_list[1]
    if num < num_list[2]:
        print(f"Minimum Number in List: {num}")
    else:
        num = num_list[2]
        print(f"Minimum Number in List: {num}")
else:
    print("Enter wrong string")


# max and min number from list with range 5
number_list = []
for x in range(0, 5):
    a = int(input("Enter Numbers: "))
    number_list.append(a)

print(number_list)
number = 0
s = input("Enter max or min: ")
if s == "max":
    if number_list[0] > number_list[1]:
        number = number_list[0]
    else:
        number = number_list[1]
    if number > number_list[2]:
        number = number
    else:
        number = number_list[2]
    if number > number_list[3]:
        number = number
    else:
        number = number_list[3]
    if number > number_list[4]:
        number = number
    else:
        number = number_list[4]
    print(f"Maximum Number in List: {number}")
elif s == "min":
    if number_list[0] < number_list[1]:
        number = number_list[0]
    else:
        number = number_list[1]
    if number < number_list[2]:
        number = number
    else:
        number = number_list[2]
    if number < number_list[3]:
        number = number
    else:
        number = number_list[3]
    if number < number_list[4]:
        number = number
    else:
        number = number_list[4]
    print(f"Minimum Number in List: {number}")
else:
    print("Enter wrong string")
