#  Write a Python program to count the occurrences of an element in a list.
new_list = []
n = int(input("Enter the limit of the list:"))
print("Enter the number to the list:")
for i in range(0,n):
    value = int(input())
    new_list.append(value)
print(new_list)
key = int(input("Enter the element:"))
count = 0
for i in new_list:
    if i == key:
        count += 1
    # print(count)
print(f"The count of {key} is {count}")