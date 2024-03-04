# Write a Python program that takes a list of integers as input and returns a
# new list with only the numbers that are prime.

import math
def primeor_not(new_list):
    res_list = []
    for n in new_list:
        r = math.isqrt(n)
        count = 0
        for i in range(2,r+1):
            if n%i == 0:
                count += 1
                break
        if count == 0:
            res_list.append(n)
    print(res_list)

# new_list = [1,2,3,4,5,6,7,47]
new_list = []
n = int(input("Enter the limit:"))
print("Enter the number:")
for i in range(n):
    num = int(input())
    new_list.append(num)
print("list of number:",new_list)
primeor_not(new_list)