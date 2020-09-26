# Object oriented programming

class Dish:
    pass

# Methods (Used with the objects)
# Static Functions (Used with the class


class StudentManagement:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def showStudent(self):
        for student in self.students:
            print("NAME> "+student.name)
            print("ROLL> "+ str(student.rollNumber))


class Student:
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber
        pass

    def study(self):
        print(self.name +" is studying")
        self.makeAnnouncement()

    def makeAnnouncement(self):
        print(self.name +' is making some announcement')


sManagement = StudentManagement()


s1 = Student("Ayesha", 190)
s2 = Student("Khurram", 191)

sManagement.addStudent(s1)
sManagement.addStudent(s2)

sManagement.showStudent()

# class Student:
#     def __init__(self, name, rollNumber):
#         self.name = name
#         self.rollNumber = rollNumber
#         pass
#
#     def study(self):
#         print(self.name +" is studying")
#
#     def makeAnnouncement():
#         print('Some announcement')
#
#
# # Student.makeAnnouncement()
#
# students = []
#
# for item in range(0,3):
#     name = input("Enter name")
#     roll = input("Enter roll")
#
#     st = Student(name, roll)
#     students.append(st)
#
#
# for student in students:
#     print("NAME > "+student.name)
#     print("ROLL > "+student.rollNumber)

# This product will have its data
# s1 = Student("Ayesha", 120)
# s1.study()
#
#
# s2 = Student("Khurram", 140)
# s2.study()

# print(s1.name)
# print(s1.rollNumber)

# s2 = Student("Khurram", 170)


# students = []
#
# for item in range(0,10):
#     st = Student()
#     students.append(st)


# print(students)

student ={
    "name" : "khurram",
    "city" : "karachi"
}

for i in [1,2,3,4,5]:
    print(i)

for i in student:
    print(student[i])