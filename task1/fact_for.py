#Find the factorial of a number taken as input using for loop
n = int(input("enter the number:"))
fact = 1
for i in range(1, n+1):
    fact = fact *i
print("factorial of number",n,"=",fact)