# Write a Python program to print the numbers of a specified listafter removing even numbers from it
# list = [24,34,53,65,78,93,23,42]
list1 = []
list2 = []
list = [24,34,53,65,78,93,23,42]
for i in list:
    if i % 2 == 0:
        list1.append(i)
        list.remove(i)
print("Even numbers:",list1)
print("list after removing the even numbers",list)
        

