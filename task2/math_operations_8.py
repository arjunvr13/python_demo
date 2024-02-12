# Define a function that accepts 2 values and return its sum, subtraction and multiplication. 
# Using 4 types of functions based on arguments and return type.
def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def product(num1,num2):
    return(num1*num2)
def division(num1,num2):
    return(num1/num2)


num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))

operation = input("Which opertion you like to perform? +,-,*,/ :")

if operation == '+':
    print(f"Sum of numbers {num1} and {num2} is {add(num1,num2)} ")
elif operation == '-':
    print(f"Subtract of numbers {num1} and {num2} is {sub(num1,num2)} ")
elif operation == '*':
    print(f"Product of numbers {num1} and {num2} is {product(num1,num2)} ")
elif operation == '/':
    print(f"Division of numbers {num1} and {num2} is {division(num1,num2)} ")
else:
    print("Invalid Operation")

