str = input("Enter the string:")
print(str)
list1 = str.split(" ")
for i in list1:
    if len(i) % 2 == 0:
        print(i,end=" ")