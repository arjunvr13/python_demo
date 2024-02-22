# Write a program to create a child class Teacher that will inherit the properties from the parent class Staff.
# attributes need for staff : role,department, salary
# attributes need for teacher: name,age
# method in staff : def print_details()
# output expected -
# Name: Raj
# Age: 28
# Role: Teacher
# Department: Science

class Staff:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def print_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Role:",self.role)
        print("Department:",self.dept)


class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # role = input("Enter the role")
        # dept = input("Enter the department")
        # salary =int(input("Enter the salary"))
        super().__init__("teacher","Science",15000)

# name = input("Enter the name:")
# age = int(input("Enter the age:"))
res = Teacher("Raj",28)
res.print_details()



