# Write a Python function that takes a list of integers as input and returns a
# new list with only the numbers that are perfect squares

import math
def perfectSquare(new_list):
    res_list = []
    other = []
    for i in new_list:
        r = math.sqrt(i)
        print(r)
        if  r.is_integer():
            res_list.append(i)
        else:
            other.append(i)
    print("list of perfect square:",res_list)
    print("list of non perfect square:",other)

new_list = []
n = int(input("Enter the limit:"))
print("Enter the number:")
for i in range(n):
    num = int(input())
    new_list.append(num)
print("list of number:",new_list)
perfectSquare(new_list)