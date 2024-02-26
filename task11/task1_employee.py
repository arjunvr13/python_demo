class Employee:
    employee_list= []
    def __init__(self,name):
        self.name = name
        self.salary = 0
        self.employee_list.append(self)


    def salary_calculate(self,hours):
        self.salary = hours*200
        return self.salary
    
    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
      
    
    def __add__(self,other):
        total_expense = self.salary + other.salary
        return total_expense
    
    @classmethod
    def average_expense(cls):
        total_employees = len(cls.employee_list)
        return total_expense/total_employees
        


class PartTimeEmployee(Employee):
    def salary_calculate(self, hours):
        self.salary = hours*150
        return self.salary


e1 = Employee('amal')
E1 = e1.salary_calculate(2)
e1.display_details()
e2 = Employee('jake')
E2 = e2.salary_calculate(4)
e2.display_details()
e3 = PartTimeEmployee('Arjun')
E3 = e3.salary_calculate(4)
e3.display_details()
total_expense = E1.__add__(E2).__add__(E3)
print("Total expenses:",total_expense)
print("Average Expense :",Employee.average_expense())
# total_expense = E1+E2+E3
# print(total_expense)