# Write a Python program to create Fibonacci series up to n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]

from functools import reduce
fib = lambda n : reduce(lambda x,_:x+[x[-2]+x[-1]],range(n-2),[0,1])

n = int(input("enter the limit :"))
print(fib(n))
print(fib(2))
print(fib(5))
print(fib(6))