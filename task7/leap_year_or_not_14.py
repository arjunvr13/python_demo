#Write a Python program to check if a given year is a leap year.
def leap_year(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0: 
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = int(input("Enter the year:"))
leap_year(year)