# Write a Python program to find the second largest number in a list.
new_list = []
n = int(input("Enter the limit of the list:"))
print("Enter the number to the list:")
for i in range(0,n):
    value = int(input())
    new_list.append(value)
print(new_list)
set_list = set(new_list)
# print('set',set_list)
list_new = list(set_list)
print("after removing duplicate value if any:",list_new)
temp = 0
length = len(list_new)
for i in range(0,length):
    for j in range(i,length):
        if new_list[i] > new_list[j]:
            temp = new_list[i]
            new_list[i] = new_list[j]
            new_list[j]  = temp
print("sorted list")
for i in range(0,length):
    print(list_new[i],end=",")
print("\nsecond largest elemet in the list:",new_list[length-2])
