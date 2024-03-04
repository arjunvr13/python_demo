# Write a Python function that takes a list of strings as input and returns a
# new list with the strings sorted in descending order of their lengths
def sorting(new_list):
    desc = sorted(new_list, key=len, reverse=True)
    print("Words in decsending order:",desc)

new_list = []
n = int(input("Enter the number of words:"))
for i in range(n):
    s = input("Enter the string:")
    new_list.append(s)
print("Words:",new_list)
sorting(new_list)
