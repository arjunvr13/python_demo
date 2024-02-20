# Write a Python program to calculate the sum of all elements in a list recursively
def sum(new_list,n):
    if n == 0:
        return 0
    else:
        return new_list[n-1] + sum(new_list,n-1)


new_list = []
n = int(input("Enter the limit of the list:"))
print("Enter the number to the list:")
for i in range(0,n):
    value = int(input())
    new_list.append(value)
print(new_list)
sum = sum(new_list,n)
print(sum)
