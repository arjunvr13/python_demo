# Write a Python program to remove duplicates from a list.
list1 = []
n = int(input("Enter the limit of the list:"))
print("Enter the number to the list:")
for i in range(0,n):
    value = int(input())
    list1.append(value)
print(list1)
check = []
dup = []
for i in list1:
    if i not in check:
        check.append(i)
    elif i not in dup:
        dup.append(i)
print("duplicate values are",*dup,end=',')
print()
print("list after removing duplicate value ",check)