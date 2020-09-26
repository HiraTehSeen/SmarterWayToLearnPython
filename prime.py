def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False


n = int(input("Enter a Number: "))
p = prime(n)
if p is False:
    print("Not Prime")
else:
    print("Prime")
