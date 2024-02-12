# Define a function that accepts lowercase words and returns uppercase words.
def to_upper(string):
    str = string.upper()
    print(str)


string = input("Enter the string:")
if string.islower():
    to_upper(string)
else:
    print("invalid")