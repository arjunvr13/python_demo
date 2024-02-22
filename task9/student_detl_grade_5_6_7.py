class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
        self.grade = self.grade_generate()
    
    def display(self):
        print(f"name:{self.name},score:{self.score}")
        

    def grade_generate(self):
        if self.score >= 90:
            return "A+"
        elif self.score >= 80 and self.score < 90:
            return "A"
        elif self.score >= 70 and self.score < 80:
            return "B+"
        elif self.score >= 70 and self.score < 60:
            return "B"
        elif self.score >= 60 and self.score < 50:
            return "C+"
        elif self.score >= 50 and self.score < 40:
            return "C"
        else:
            return "FAILED"
    
    def as_dict(self):
        return {"Name" : self.name, "Score" :self.score, "Grade" :self.grade}

stu1 = Student("vimal",90)
stu2 = Student("amal",88)
stu1.display()
stu2.display()
print(stu1.as_dict())
print(stu2.as_dict())
