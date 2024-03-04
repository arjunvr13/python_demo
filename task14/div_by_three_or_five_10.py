# Write a Python function that takes a list of numbers as input and returns
# the sum of all the numbers divisible by 3 or 5. 

def sumOfList(new_list):
    result = sum(x for x in new_list if x % 3 ==0 or x % 5 == 0)
    return result

new_list = []
n = int(input("Enter the limit:"))
print("Enter the number:")
for i in range(n):
    num = int(input())
    new_list.append(num)
print("list of number:",new_list)
res = sumOfList(new_list)
print("Sum of all the numbers divisible by 3 or 5:",res)