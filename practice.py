# a = [1, "Fsd", 23.1, "Lhr", 5, ]
# print(a[2])
#
# # dictionaries with in dictionary
# b = {1: {"Flower": "Rose", "Color": "Red"},
#      2: {"Flower": "Lily", "Color": "White"},
#      3: {"Flower": "Jasmin", "Color": "Purple"}}
# print(b[2])
# # get info through outer dic key within another dic
# print(b[3]["Color"])

# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed data types
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = {1, "Hello", 26, 3.1}
print(my_set)


# print python
for char in 'PYTHON STRING':
    if char == ' ':
        break
    print(char, end='')

    if char == 'O':
        continue

# check sum
i = sum = 0
while i <= 4:
    sum += i
    i = i+1
print(sum)