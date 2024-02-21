f1 = open("text","r")
n = int(input("Enter the number:"))
for i in range(n):
    print(f1.readline(), end='')
f1.close()