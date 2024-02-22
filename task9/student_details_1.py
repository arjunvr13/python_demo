# Write a program to create a class by name Students, and initialize attributes like name, age, and grade while creating an object. 

class Student_details:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def details_print(self):
        print("name =",self.name)
        print("age =",self.age)
        print("grade =",self.grade)


n = int(input("Enter the number of students:"))
for i in range(0,n):
    name = input("Enter the name of the student:")
    age = int(input("Enter the age:"))
    grade = input("Enter the grade as A+,A,B+,B,C,C+:,")
    stud = Student_details(name,age,grade)
    stud.details_print()