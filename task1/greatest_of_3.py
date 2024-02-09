a = int(input("enter the first number ="))
b = int(input("enter the second number ="))
c = int(input("enter the third number ="))
if(a > b) and (a > c):
    print("first number =",a,",is the largest")
elif(b > a) and (b > c):
    print("second number =",b,",is the largest")
elif(a == b == c):
    print("all are equal")
else:
    print("third number =",c,",is the largest")

