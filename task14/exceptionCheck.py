def check():
    try:
        num = int(input("Enter the number:"))
        if isinstance(num,int):
            print(num)
        else:
            raise ValueError
    except ValueError:
        print(f"Invalid Input..Please Input Integer Only..")
        
