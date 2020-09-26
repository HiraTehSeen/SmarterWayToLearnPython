# Example 1
# retrieving values from list
# employee_data = ['Ali', 125000, 'Google', 5]
# print(f"{employee_data[0]} is working in {employee_data[2]} for {employee_data[3]} years and his salary is
# {employee_data[1]}")

# Example 2
# studentData = ['Ahmed', 'Bilal', 'Government College University', 'Computer Science', 'BS', 50000,
#                '28 January 2020', '05 February 2020']
# print(f"Hello {studentData[0]} {studentData[1]} , \n Your Application is accepted for admission in "
#       f"\"{studentData[4]} {studentData[3]}\" in {studentData[2]}. \n You have to submit fee {studentData[5]} "
#       f"before {studentData[6]}. \n Your classes will start from {studentData[7]}. \n Thanks'")

# Slicing
# cities = ["Faisalabad", "Lahore", "Islamabad", "Peshawar", "Quetta", "Sahiwal", "Rawalpindi", "Sialkot"]

# +ve slicing
# print(cities[0: 4])
# print(cities[2: 6])
# print(cities[5: 8])

# -ve slicing
# print(cities[-4: -1])
# print(cities[-5: ])

# Update list
# studentData = ["Ali Raza", 22, 91.24, "Computer Science", 5, "University of Agriculture"]
# print(studentData)

# append
# studentData.append('20 February 2019')
# studentData.append(8)
# print(studentData)

# insert
# studentData.insert(4, 25000)
# studentData.insert(1, 'M. Iqbal')
# print(studentData)

# update
# studentData[0] = 'Zohaib Ali'
# studentData[6] = 7
# print(studentData)

# remove
# studentData.remove('Computer Science')
# studentData.remove(91.24)
# print(studentData)

# # Multi-dimensional
# employeeData = [["Ali", 35000, "Software Engineer"], ["Talha", 55000, "Product Manager"],
#                 ["Nasir", 79000, "Computer Engineer"], ["Khalid", 44000, "DBA"]

# How many times will the if statement run? Answer with a numeral.
chosen_letter = "b"
letter_list = ["a", "b", "c", "d", "e", "f"]
for a_letter in letter_list:
    if a_letter == chosen_letter:
        print("It's a match.")
        break
