try:
    n = int(input("Enter the number:"))
    print(n)
    if n.is_integer():
        print('digit')
except ValueError:
    print('Only accept integers')