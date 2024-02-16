b = int(input("Enter the number of boys:"))
boys = {}
while len(boys) < b:
    roll_number = int(input("Enter the roll number:"))
    name = input("Enter the name:")
    if roll_number not in boys:
        boys[roll_number] = name
    else:
        print("value already exists")

print("boys:",boys)

g = int(input("Enter the number of girls:"))
girls = {}
while len(girls) < g:
    roll_number = int(input("Enter the roll number:"))
    name = input("Enter the name:")
    if roll_number not in boys:
        girls[roll_number] = name
    else:
        print("value already exists")
print("girls:",girls)
boys.update(girls)
print(boys)
