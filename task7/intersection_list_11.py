# Write a Python program to find the intersection of two lists
def list_create():
    n = int(input("Enter the limit of the list:"))
    listt= []
    print("Enter the number to the list:")
    for i in range(0,n):
        value = int(input())
        listt.append(value)
    return(listt)
def checkup(list1,list2,list3):
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)
    return(list3)

list1 = list_create()
list2 = list_create()
list3 = []
result = checkup(list1,list2,list3)
print(list1)
print(list2)
print("Common elements in both the list are",result)