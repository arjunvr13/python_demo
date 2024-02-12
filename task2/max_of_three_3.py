# Write a Python function to find the maximum of three numbers
def maxof_three(a,b,c):
    if(a > b) and(a > c):
        print("frist number",a,"is the largest")
    elif(b > a) and (b > c):
        print("second number",b,"is the largest")
    else:
        print("third number",c,"is the largest")

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
maxof_three(a,b,c)