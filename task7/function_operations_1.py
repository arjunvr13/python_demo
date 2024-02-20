def sum(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def pro(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def floor(a,b):
    return(a//b)
def expon(a,b):
    return(a**b)


while True:
    n1 = int(input("Enter the first number:"))
    n2 = int(input("Enter the second number:"))
    operation = input("What operation do you like to perform? +,-,*,/,//,** :")
    if operation == "+":
        print(f"Sum of {n1} and {n2} = {sum(n1,n2)}")
    elif operation == "-":
        print(f"Subtract of {n1} and {n2} = {sub(n1,n2)}")
    elif operation == "*":
        print(f"Product of {n1} and {n2} = {pro(n1,n2)}")
    elif operation == "/":
        print(f"Division of {n1} and {n2} = {div(n1,n2)}")
    elif operation == "//":
        print(f"Floor of {n1} and {n2} = {floor(n1,n2)}")
    elif operation == "**":
        print(f"Exponent of {n1} and {n2} = {expon(n1,n2)}")
    else:
        print("Invalid Entry")
        continue

    contin = input("Enter do you want to continue yes or no? ")
    if contin.lower() != 'yes':
        break 


