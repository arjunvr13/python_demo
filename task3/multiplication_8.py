# Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22

list1 = [2, 4, 6, 9, 11]
n = int(input("enter the number:"))
str = list(map(lambda num:num * n,list1))
print(str)