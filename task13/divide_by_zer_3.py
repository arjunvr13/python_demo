num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the Second number:"))
try:
    div = num1/num2
    print(div)
except ZeroDivisionError:
    print("Number cannot be divided by Zero")