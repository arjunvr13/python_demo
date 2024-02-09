n = float(input("enter the number"))
if(n % 2 == 0):  
    print("Even Number")
elif(isinstance(n,float)):
    print("invalid")
elif((n % 2 == 1)):
    print("Odd Number")