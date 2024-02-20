n = int(input("Enter the number:"))
divisors = [n,]
for i in range(1,(n//2)+1):
    if n%i == 0:
        divisors.append(i)
if sum(divisors)-n == n:
    print(n,"is a perfect number")
else:
    print("not a perfect number")

    
