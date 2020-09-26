class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def study(self):
        print(self.name + " is Studying")

    def list(self):
        l.append(self.name)
        l.append(self.city)


l = []
while True:
    a = input("Enter Options: ")
    if a == '1':
        n = input("Enter Name: ")
        c = input("Enter City: ")
        s1 = Student(n, c)
        print(s1.name)
        print(s1.city)
        s1.study()
        s1.list()
    else:
        break
print(l)
