# Write a Python program to count the number of occurrences of each element in a tuple.
# tuple = ('a','b','c','a','b')
def convert(t):
    unique = list(t)
    dict = {}
    print('hai')
    for i in unique:
        if i != ' ':
            dict[i] = unique.count(i)
    return(dict)

# new_list = []
# n = int(input("Enter the limit of the list:"))
# print("Enter the number to the list:")
# for i in range(0,n):
#     value = int(input())
#     new_list.append(value)
# print(new_list)
# t = tuple(new_list)
t = ('a','b','c','a','b')
con = convert(t)
print(t)
print(con)
