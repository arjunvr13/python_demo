# Create a function that takes two arguments, a name and an age, and prints a message like
#  "Hello, [Name]! You are [Age] years old." Call this function with your name and age as arguments

def candidate_info(name, age):
    print("Hello, "+name+"! You are",age,"years old.")



name = input("enter the name of the candidate :")
age = int(input("enter the age of the candidate :"))
candidate_info(name,age)