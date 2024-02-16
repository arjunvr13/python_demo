# Write a Python program to get the maximum and minimum values of a dictionary
student = {}
n = int(input("Enter the number:"))
while len(student) < n:
    student_name = input("Enter the name of the student:")
    mark = int(input("Enter the mark in 100:"))
    if mark >100:
        print("Invalis entry,re enter")
        mark = int(input("Enter the mark in 100:"))
    if student_name not in student:
        student[student_name] = mark
    else:
        print("name already exists")
print(student)
print("Maximum value in the dictionary:",max(student.values()))
print("Mininum value in the dictionary:",min(student.values()))
