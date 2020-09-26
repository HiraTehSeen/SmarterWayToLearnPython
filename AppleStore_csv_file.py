# numpy library used
# import numpy as np
# nums = np.arange(1,5)
# for i in nums:
#     print(i)


# Read excel file
import csv

with open('AppleStore.csv',encoding="utf8") as file:
    myData = csv.reader(file)
    convertedData = list(myData)
    # print(convertedData)
    # print(convertedData)
    #
    # totalRating = 0
    # educationRows = 0
    price_categories = []

    for item in convertedData[1:]:
        price = float(item[4])
        if price == "0":

            if 'free' not in price_categories:
                price_categories.append("free")

        elif price > 2 and price < 5:
            if "cheap" not in price_categories:
                price_categories.append("cheap")

        elif price > 5 and price < 20:
            if "normal" not in price_categories:
                price_categories.append("normal")

        elif price > 20:
            if "expensive" not in price_categories:
                price_categories.append("expensive")

    print(price_categories)
    #     genre = item[11]
    #     if genre == "Education" or genre == "Games":
    #         educationRows = educationRows + 1
    # print(educationRows)
    #     totalRating +=  float(item[7])
    #     # print(item[7])
    #
    # average_rating = totalRating / len(convertedData)
    # print(average_rating)
