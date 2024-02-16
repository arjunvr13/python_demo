# Write a Python program to sum all the items in a dictionary
n = int(input("Enter the number of key, value pairs:"))
dict = {}
while len(dict) < n:
    emp_id = int(input("Enter the employee id:"))
    salary = int(input("Enter the salary:"))
    if emp_id not in dict:
        dict[emp_id] = salary
    else:
        print("id already exists")
print("Sum of salary=",sum(dict.values()))