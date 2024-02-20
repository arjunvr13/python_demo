# Write a Python program to remove all occurrences of a given element from a list.
new_list = []
n = int(input("Enter the limit of the list:"))
print("Enter the number to the list:")
for i in range(0,n):
    value = int(input())
    new_list.append(value)
print(new_list)
element = int(input("Enter th element to be removed:"))
for i in new_list:
    if i == element:
        new_list.remove(i)
print(new_list)
