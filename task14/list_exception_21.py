# Write a Python program that executes an operation on a list and handles an
# IndexError exception if the index is out of range.

# limit = int(input("Enter the limit of the list:"))
list_new = [1,2,3,4]
print("length of the list=",len(list_new))
try:
    index = int(input("The index at which the value need to be displyed:"))
    print(list_new[index])
    raise IndexError
except IndexError:
    print("list index out of range")