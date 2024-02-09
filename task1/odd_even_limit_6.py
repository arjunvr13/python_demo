# Python program to print all even/odd numbers in the range given by user
n = int(input("Enter the limit="))
select = input("ood/even:")
if(select == "even"):
    for i in range(n):
        if i % 2 == 0:
            print(i,end=",")
else:
    for i in range(n):
        if i % 2 == 1:
            print(i,end=",")
    
    

