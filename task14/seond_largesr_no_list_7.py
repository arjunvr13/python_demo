# Write a function that takes a list of numbers as input and returns the
# second-largest number. 
def second_largest(new_list):
    new_list.sort()
    print(new_list)
    print("second largest number",new_list[-2])


new_list = []
n = int(input("Enter the limit:"))
print("Enter the number:")
for i in range(n):
    num = int(input())
    new_list.append(num)
print("list of number:",new_list)
duplicate_remove = set(new_list)
convert_list = list(duplicate_remove)
second_largest(convert_list)