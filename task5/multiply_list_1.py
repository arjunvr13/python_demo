list1 = []
n = int(input("Enter the numbers of elements:"))
print("Enter the numbers:")
multiply = 1
for i in range(0,n):
    list2 = int(input())
    list1.append(list2)
print(list1)
for x in list1:
    multiply *= x
print(multiply)