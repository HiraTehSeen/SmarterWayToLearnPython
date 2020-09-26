name = "Khurram"


def printName():
    print(name)


def changeName(new):
    name = new
    return name


printName()
name = changeName("Ali")
printName()
