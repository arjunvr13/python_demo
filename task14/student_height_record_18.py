# Python program to for student height record for a school using Class and
# Objects
class Student:
    def __init__(self):
        self.student_record = {}
        

    def addStudent(self, name, height):
        self.student_record[name] = height

    def findStudent(self, name):
        if name in self.student_record:
            return self.student_record[name]
        else:
            return None
    
    def displayAllStudent(self):
        print("\nStudent Details")
        for name, height in self.student_record.items():
            print(f"name:{name} ,height:{height}cm")
    

school_record = Student()
while True:
    print("\n1. Add Student Height")
    print("2. Find Student Height")
    print("3. Display all Records")
    print("4. Quit")
    choice = int(input("Enter your choice:"))
    

    if choice == 1:
        name = input("\nEnter the name:")
        height = int(input("Enter th height in cm only:"))
        school_record.addStudent(name,height)
        print(f"{name}'s height added to record")

    elif choice == 2:
        name = input("\nEnter the name of the student to be searched:")
        height = school_record.findStudent(name)
        if height is not None:
            print(f"{name}'s height is {height}cm")
        else:
            print(f"{name} not found")
    
    elif choice == 3:
        school_record.displayAllStudent()
    
    elif choice == 4:
        break

    else:
        print("\nInvalid Choice")





# class Student:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
    
#     def displayInfo(self):
#         print(f"name:{self.name}:height:{self.height}")

# def displayAllStudent(student_list):
#     for student in student_list:
#         student.displayInfo()

# student_list = []
# choice = 'y'
# while choice == 'y':
#     name = input("Enter the name:")
#     height = int(input("Enter the height in cm only:"))
#     obj = Student(name,height)
#     student_list.append(obj)
#     choice = input("Add another Student?(y/n):")
    


# displayAllStudent(student_list)