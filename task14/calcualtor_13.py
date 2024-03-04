# Implement a program that simulates a basic calculator, allowing users to
# perform arithmetic operations (addition, subtraction, multiplication,
# division) on two numbers

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b

choice = 1
while choice != 0:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    try:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        obj = Calculator(a,b)
        if choice == 1:
            print(f"Addition of {a} and {b} = ",obj.add())
        elif choice == 2:
            print(f"Subtraction of {a} and {b} = ",obj.sub())
        elif choice == 3:
            print(f"Product of {a} and {b} = ",obj.mul())
        elif choice == 4:
            print(f"Division of {a} and {b} = ",obj.div())
        elif choice == 5:
            print("Exiting")
            break
        else:
            print("Invalid choice")
    except ValueError as e:
        print(e)