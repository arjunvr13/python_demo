# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and prints the result.
sum = lambda a : a + 15
product = lambda x,y : x * y
n = int(input("Enter the number to be added to 15:"))
a = int(input("Enter the number  a:"))
b = int(input("Enter the number  b:"))
print(sum(n))
print(product(2,3))