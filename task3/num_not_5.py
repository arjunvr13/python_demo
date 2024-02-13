# Write a Python program to check whether a given string is a number or not using Lambda

str = lambda a : a.isnumeric()
s = input("enter the string:")
if str(s) is True:
    print("Number")
else:
    print("not a number")
