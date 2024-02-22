# Write a program that prints the class name using its object.
# class School:
#     def name_school(self,school):
#         print('name:',school)
    
# name = input("Enter the name of the school:")
# sch = School()
# sch.name_school(name)
# print("Name of the class:"type(sch).__name__)

class School:
    pass

sch = School()
print("Name of the class:",type(sch).__name__)
 