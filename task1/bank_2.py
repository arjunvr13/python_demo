# Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw, 
#      print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. 
#      if balance is below 500 print an alert message : your account balance is "available_balance", Please  keep your account balance above Rs.500 to avoid unwanted charges.
# # min_balance = 500
# amount = int(input("Enter the amount to withdraw :"))
# balance = min_balance - amount 
# print( balance)
# if(amount > min_balance):
#     print("insufficinet balance")
# elif(balance < min_balance):
#     print(" your account balance is ",balance,", Please  keep your account balance above Rs.500 to avoid unwanted charges.")

main_balance = 1000
min_balance = 500
amount = int(input("Enter the amount to withdraw :"))
balance = main_balance - amount
if(amount > main_balance) or (amount > min_balance):
     print("insufficient balance")
     print("account balance",balance)
elif balance <=500:
        print(" your account balance is ",balance,", Please  keep your account balance above Rs.500 to avoid unwanted charges.")
else:
    print("account balance",balance)
