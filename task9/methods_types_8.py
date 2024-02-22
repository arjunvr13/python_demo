# show class method, static method and instance method with simple example.

class Student:
    school = "beinex"
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name


    def student_details(self):
        print("roll no:",self.roll_no)
        print("name:",self.name)

    @classmethod
    def school_info(cls):
        return cls.school
    
    @staticmethod
    def conclusion():
        return "They both study in the same school"

st1 = Student(1,"Abhijith")
st2 = Student(2,"Amal")
st1.student_details()
print("School:",Student.school_info())
st2.student_details()
print("School:",Student.school_info())
print(Student.conclusion())