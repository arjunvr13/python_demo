# Define a function that accepts roll number and returns whether the student is present or absent.

def student_add(roll_number):
    list = [1,2,3,4]
    print(list)
    list.append(roll_number)
    print(list)
    return(list)
    
def present(e,p):
    if e in p:
        return(print("roll number",e,"is present"))
    else:
        return(print("absent"))

roll_number = int(input("Enter the roll number:"))
p = student_add(roll_number)
e = int(input("Enter the roll number to be checked:"))
present(e,p)

