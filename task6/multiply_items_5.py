# Write a Python program to multiply all the items in a dictionary.
n = int(input("Enter the number of key, value pairs:"))
dict = {}
while len(dict) < n:
    product = input("Enter the name of the product:")
    number = int(input("Enter the number:"))
    if product not in dict:
        dict[product] = number
    else:
        print("id already exists")
print(dict)
product = 1
for i in dict.values():
    product *= i 
print("The product of all the values in the dictionary:",product)