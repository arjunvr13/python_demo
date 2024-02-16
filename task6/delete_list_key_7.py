# Write a Python program to Delete a list of keys from a dictionary
cars = {}
n = int(input("Enter the number:"))
while len(cars) < n:
    name = input("Enter the name of the car:")
    year = int(input("Enter the year of manufacturing:"))
    if name not in cars:
        cars[name] = year
    else:
        print("the name already exists")
print(cars)
list1 = []
n = int(input("Enter the number:"))
print("Enter car names")
for n in range(0, n):
    list1.append(input())
print(list1)

for car in list1:
    if car in cars:
        cars.pop(car)
    else:
        print("invalid input: ", car)
print("Items after removing:",cars)