import csv
myFile = open("artworks_clean.csv", encoding="utf-8")
myData = csv.reader(myFile)

listedData = list(myData)


def formatFunction(milliseconds):
    milliseconds = int(milliseconds)
    seconds = (milliseconds/1000) % 60
    seconds = int(seconds)
    minutes = (milliseconds/(1000*60)) % 60
    hours = (milliseconds/(1000 * 60 * 60)) % 24
    return ("%d:%d:%d" % (hours, minutes, seconds))

# check time change it
# for item in listedData[1:]:
#       if len(item) > 8:
#         formattedTime = formatFunction(item[8])
#         print(formattedTime)

# calculate ages above 40 nationality
ages = []

for item in listedData[1:]:


    dob = item[3]

    if  dob == '':
        ages.append(0)
    else:
        dob = int(item[3])
        endDate = int(item[-2])
        diff = endDate - dob

        ages.append(diff)

        # print(diff)

# print(ages)


def getNationaityByAge(ages):

    nationalities = []

    for index,age in enumerate(ages):
        if age > 40:
            nationalities.append(listedData[1:][index][2])

    return nationalities

myNatnilaities = getNationaityByAge(ages)

print(myNatnilaities)


for nat in myNatnilaities:
    myNationlaitiesDic[nat] = myNatnilaities.count(nat)
    # if nat in myNationlaitiesDic:
    #     myNationlaitiesDic[nat] = myNationlaitiesDic[nat] +1
    # else:
    #     myNationlaitiesDic[nat] = 1


print(myNationlaitiesDic)
