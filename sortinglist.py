# # using sort function min and max number find
# n = input("Enter Multiple Number by using (,): ")
# number = n.split(',')
# print(number)
# number.sort()
# print(number)
# user_string = input("Enter min or max: ")
# if user_string == "max":
#     print(number[-1])
# elif user_string == "min":
#     print(number[0])
# else:
#     print("Wrong String")


# using built in function of min and max
num_list = []
for i in range(1, 11):
    num = int(input("Enter Number: "))
    num_list.append(num)
print(num_list)
s = input("Enter min or max: ")
a = 0
if s == "max":
    a = max(num_list)
    print(a)
elif s == "min":
    a = min(num_list)
    print(a)
else:
    print("Enter wrong String")