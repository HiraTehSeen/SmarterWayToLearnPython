# # Set this program according to MCQs it display a output
# fo = open("foo.txt", "rw+")
# print("Name of the file: ", fo.name)
#
# # Assuming file has following 5 lines
# # This is 1st line
# # This is 2nd line
# # This is 3rd line
# # This is 4th line
# # This is 5th line
#
# for index in range(5):
#     line = fo.next()
#     print("Line No %d - %s" % (index, line))
#
# # Close opened file
# fo.close()


# # Exception Handling MCQs
try:
    print("1")
except:
    print("2")
finally:
    print("3")
