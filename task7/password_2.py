import re
def password_check(passkey):
    if len(passkey) < 8:
        msg = "should contain mininum of 8 characters" 
    elif not re.search("[a-z]",passkey):
        msg = "should contain a-z"  
    elif not re.search("[A-Z]",passkey):
        msg = "should contain A-Z"
    elif not re.search("[0-9]",passkey):
        msg = "should contain numeric value"
    elif not re.search("[_@$]",passkey):
        msg = "should contain _@$"
    else:
        return True, None
    
            
    print(msg)
    return False, msg

while True: 
    passkey = input("Enter the password:")
    flag_check, msg = password_check(passkey)
    if not flag_check:
        print(f"invalid password. {msg}")
    else:   
        print("Valid password")
    contin = input("Do you want to check another password? y/n:")
    if contin.lower() != 'y':
        break