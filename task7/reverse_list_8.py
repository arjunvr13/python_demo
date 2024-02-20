# Write a Python program to reverse a list.

# new_list = []
# n = int(input("Enter the limit of the list:"))
# print("Enter the number to the list:")
# for i in range(0,n):
#     value = int(input())
#     new_list.append(value)
# print(new_list)
# length= len(new_list)
# print(length)
# print(new_list[::-1])

new_list = []
n = int(input("Enter the limit of the list:"))
print("Enter the number to the list:")
for i in range(0,n):
    value = int(input())
    new_list.append(value)
print(new_list)
length= len(new_list)
list_ans = []
for i in range(length,0,-1):
    list_ans.append(i)
print(list_ans)