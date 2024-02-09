# Find the sum of all even numbers between the range given by user
start = int(input("enter the start:")) 
end = int(input("enter the end:"))
sum = 0
for i in range(start,end+1):
    if i % 2 == 0:
        sum += i
print(sum)