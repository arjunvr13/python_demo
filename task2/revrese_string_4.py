# Write a Python program to reverse a string
def reverse_string(s):
    str = ""
    for i in s:
        str = i + str
    return(str)

s = input("Enter the string:")
print(reverse_string(s))