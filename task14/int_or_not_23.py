try:
    n = int(input("Enter the number:"))
    if isinstance(n,int):
        print(n)
    else:
        raise ValueError
except ValueError:
    print("Invalid Input..Please Input Integer Only..")