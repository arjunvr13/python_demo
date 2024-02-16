# Write a Python program to get dictionary keys as a list
n = int(input("Enter the number of employees:"))
employee = {}
while len(employee) < n:
    name = input("Enter the name of the employee:")
    salary = int(input("Enter the salary:")) 
    if name not in employee:
        employee[name] = salary
    else:
        print("name already exists")
print(employee)
list1 = employee.keys()
print(list1)