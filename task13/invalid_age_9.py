class InvalidAgeError(Exception):
    pass

def age_check(age):
    try:
        if 0 < age > 150:
            raise InvalidAgeError
        else:
            print("Valid")
    except InvalidAgeError:
        print("Invalid age")
 
age = int(input("Enter the age:"))
age_check(age)
