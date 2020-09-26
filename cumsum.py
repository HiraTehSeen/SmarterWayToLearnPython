# # cumulative sum of number
# def sum(v):
#     total = 0
#     for i in v:
#         total += int(i)
#         n.append(total)
#     return n
#
#
# # collect number that start from same digit
# def sep(v):
#     op = input("Which number you want: ")
#
#     for item in v:
#         if item[0] == op:
#             s.append(item)
#     return s
#
#     # if op == '0':
#     #     for j in v:
#     #         if int(j) < 10:
#     #             s.append(int(j))
#     #     return s
#     # elif op == '1':
#     #     for j in v:
#     #         if 10 <= int(j) < 20:
#     #             s.append(int(j))
#     #     return s
#     # elif op == '2':
#     #     for j in v:
#     #         if 20 <= int(j) < 30:
#     #             s.append(int(j))
#     #     return s
#     # elif op == '3':
#     #     for j in v:
#     #         if 30 <= int(j) < 40:
#     #             s.append(int(j))
#     #     return s
#     # elif op == '4':
#     #     for j in v:
#     #         if 40 <= int(j) < 50:
#     #             s.append(int(j))
#     #     return s
#     # else:
#     #     print("Wrong")
#
#
# s = []
# n = []
# num = input("Enter Number: ")
# val = num.split(",")
# res = sum(val)
# print(res)
# r = sep(val)
# print(r)
