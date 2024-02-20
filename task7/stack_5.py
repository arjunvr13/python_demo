# Write a Python program to implement a stack using a list.(push and pop)
def stack():
    new_list = []
    n = int(input("Enter the number of elements :"))
    print("Enter the number to the stack:")
    for i in range(0,n):
        value = int(input())
        new_list.append(value)
    print(new_list)
    return(new_list)

def push(list1):
    new = int(input("Enter the element to be pushed:"))
    list1.append(new)
    return(list1)

def popo(list1):
    length = len(list1)
    # print(length)
    if length != 0:
        list1.pop(length-1)
    else:
        print("stack empty")
    return(list1)                                                                          
        

while True:
    print("Select the operation to be performed",end='\n')
    print("create")
    print("push")
    print("pop")
    operation = input("Enter the operation:")
    if operation == 'create':
        list1 = stack()
    elif operation == 'push':
        push(list1)
        print(list1)
    elif operation == 'pop':
        popo(list1)
        print(list1)
    else:
        print("Invalid Entry")
    contin = input("Enter do you want to continue yes or no? ")
    if contin.lower() != 'yes':
        break 