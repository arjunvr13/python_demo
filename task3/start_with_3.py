# Write a Python program to find if a given string starts with a given character using Lambda.?
def check(str,char):
    start = lambda a : a.startswith(char)
    print(start(str))
str = input("Enter the string to be checked :")
char = input("Enter the Character:")
check(str,char)