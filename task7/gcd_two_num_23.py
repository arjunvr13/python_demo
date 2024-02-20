n1 = int(input("Enter the First number:"))
n2 = int(input("Enter the Second number:"))
small = 0
gcd = 0
if n1 < n2 :
    small = n1
else:
    small = n2
for i in range(1,(small//2)+1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i
print("gcd:",gcd)


