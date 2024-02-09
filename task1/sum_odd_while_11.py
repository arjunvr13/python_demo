# Find the sum of all odd numbers between the rane given by user using while loop
def sumOf(s,e):
    sum = 0
    while s <= e:
        if s % 2 == 1:
            sum += s
        s += 1 
    return sum



start= int(input("enter the start:")) 
end = int(input("enter the end:"))
result = sumOf(start,end)
print(result)