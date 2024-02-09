def factorial(n):
    fact = 1
    while n >= 1:
        fact = fact * n 
        n = n - 1
    return fact


f = int(input("enter the number:"))
result = factorial(f)
print(result)