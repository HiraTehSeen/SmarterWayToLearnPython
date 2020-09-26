def get_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    city = input("Enter City: ")
    salary = int(input("Enter Salary: "))
    user = {"name": name, "email": email, "city": city, "salary": salary}
    return user


list_user = []
t = 0
while True:
    a = input("Enter Option: ")
    if a == '1':
        dis_user = get_user()
        list_user.append(dis_user)
    elif a == '2':
        print(list_user)
    elif a == '3':
        user = input("Find user: ")
        for item in list_user:
            if item["name"] == user:
                print(item)
                break
        else:
            print("Not Found")
        break
    elif a == '4':
        user = input("Find user: ")
        for item in list_user:
            if item["name"] == user:
                item["name"] = input("Enter Name: ")
                item["email"] = input("Enter Email: ")
                item["city"] = input("Enter City: ")
                item["salary"] = int(input("Enter Salary: "))
                break
        print(list_user)
    elif a == '5':
        for i in list_user:
            if i["salary"]:
                t += i["salary"]
        print(t)
    else:
        print("Enter Wrong Option")
        break
