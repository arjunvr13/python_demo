# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words
#  in a hyphen-separated sequence after sorting them alphabetically.
#  Sample Items : green-red-yellow-black-white Expected Result : black-green-red-white-yellowu

def sort_string(p):
    o = sorted(p)
    t = '-'.join(o)
    print(t)

s = input("Enter the string with hypen:")
print(s)
p = s.split("-")
# print(p)
# print(type(p))
sort_string(p)
