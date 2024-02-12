def fact(n):
    fact = 1
    while n >= 1:
        fact = fact * n
        n = n - 1
    return fact



n = int(input("Enter the number :"))
print("Factorial of number",n,"=",fact(n))