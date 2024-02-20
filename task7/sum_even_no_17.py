# Write a Python program to find the sum of all even numbers in a list

new_list = []
n = int(input("Enter the limit of the list:"))
print("Enter the number to the list:")
for i in range(0,n):
    value = int(input())
    new_list.append(value)
print(new_list)
sum = 0
for i in range(0,n):
    if new_list[i] %2 ==0:
        sum += new_list[i] 
print(sum)