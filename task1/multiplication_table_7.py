# Python program to print the multiplication table of any number (number should be taken as input and user decides the end limit of the table)
n = int(input("enter the number= "))
start = int(input("enter the starting number= "))
end = int(input("enter the ending number= "))
for i in range(start,end+1):
    print(n, 'x', i, '=', n*i)