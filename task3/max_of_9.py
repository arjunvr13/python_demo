# Write a Python program to find the maximum value in a given heterogeneous list using lambda.Original list:
# ['Python', 3, 2, 4, 5, 'version']

list1 = ['Python', 3, 2, 4, 5, 'version']
res = max(filter(lambda x : isinstance(x,int),list1))
print(list1)
print("Maximum value in the list:",res)