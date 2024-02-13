# Write a Python program to create a function that takes one argument,
# and that argument will be multiplied with an unknown given number
def product(n):
    prod = lambda a : a * n
    num = int(input("Enter the second number:"))
    print("product:",prod(num))



n = int(input("Enter the first number:"))
product(n)