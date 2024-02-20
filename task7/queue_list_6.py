# Write a Python program to implement a queue using a list.(enqueue and dequeue)
def create_queue():
    new_queue = []
    n = int(input("Enter the number of elements :"))
    print("Enter the number to the stack:")
    for i in range(0,n):
        value = int(input())
        new_queue.append(value)
    print(new_queue)
    return(new_queue)
def enque(queue):
    new = int(input("Enter the element to be pushed:"))
    queue.append(new)
    return(queue)
def deque(queue):
    queue.pop(0)
    return(queue)



while True:
    print("Select the operation to be performed",end='\n')
    print("create")
    print("enqueue")
    print("dequeue")
    operation = input("Enter the operation:")
    if operation == 'create':
        queue = create_queue()
        print(deque)
    elif operation == 'enqueue':
        enque(queue)
        print(queue)
    elif operation == 'dequeue':
        deque(queue)
        print(queue)

    contin = input("Enter do you want to continue yes or no? ")
    if contin.lower() != 'yes':
        break 
    