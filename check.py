# # dictionary that show output length
# total = {}
# def insert(items):
#     if items in total:
#         total[items] += 1
#     else:
#         total[items] = 1
#
#
# insert('Apple')
# insert('Ball')
# insert('Apple')
# print(len(total))
# print(total)

# # dictionary
# test = {1: 'A', 2: 'B', 3: 'C'}
# del test[1]
# test[1] = 'D'
# del test[2]
# print(len(test))
# print(test)

# # dictionary
# count = {}
# count[(1, 2, 4)] = 5
# count[(4,2,1)] = 7
# count[(1,2)] = 6
# count[(4,2,1)] = 2
# print(count)
# tot = 0
# for i in count:
#     tot=tot+count[i]
# print(len(count)+tot)

# # MCQS Function
# def foo(i, x=[]):
#     x.append(x.append(i))
#     return x
# for i in range(3):
#     y = foo(i)
# print(y)


# # MCQs Local and Global Function
# def f1(x):
#     # global x
#     x+=1
#     print(x)
# f1(15)
# print("hello")

# # MCQs classes
# class test:
#     def __init__(self):
#         self.variable = 'Old'
#         self.Change(self.variable)
#     def Change(self, var):
#         var = 'New'
# obj=test()
# print(obj.variable)


# # MCQs classes
# def add(c, k):
#     c.test = c.test + 1
#     k = k + 1
#
# class A:
#     def __init__(self):
#         self.test = 0
#
# def main():
#     Count = A()
#     k = 0
#
#     for i in range(0, 25):
#         add(Count, k)
#     print("Count.test=", Count.test)
#     print("k =", k)
#
# main()

# # MCQs classes
# class B(object):
#   def first(self):
#     print("First method called")
#   def second(self):
#     print("Second method called")
# ob = B()
# B.first(ob)

