# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
import math
def prime_not(n):
    r = math.isqrt(n)
    count = 0
    for i in range(2,r+1):
        if (n % i == 0):
            count += 1
            break
    if count != 0:
        print("not prime")
    else:
        print("prime")


n = int(input("Enter the number:"))
prime_not(n)