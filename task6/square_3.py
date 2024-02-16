# Write a Python program to print a dictionary where the keys are numbers between 1 and 15 
# (both included) and the values are the square of the keys
limit = int(input("Enter the limit:"))
dict_square = {x : x**2 for x in range(1,limit+1)}
print(dict_square)