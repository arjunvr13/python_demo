# Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
# 	lst1=[2, 4, 6, 8, 10, 12, 14]
list1=[2, 4, 6, 8, 10, 12, 14]
new = [i * i for i in list1 if i * i >50]
print(new)