class NegativeBalanceError(Exception):
    pass
class BankAccount:
    def __init__(self, balance,withdraw):
        self.balance = balance
        self.withdraw = withdraw
        self.minimum = 0


    def balance_check(self):
        self.minimum = self.balance - self.withdraw
        try:
            if self.minimum <= 0:
                # print(f"balance :{self.minimum}")
                raise NegativeBalanceError
            else:
                print(f"balance :{self.minimum}")
        except NegativeBalanceError:
            print("Insufficinet balance")
        except Exception as e:
            print(e)


balance = 5000
withdraw = int(input("Enter the amount to be withdrawn:"))
bank = BankAccount(balance,withdraw)
bank.balance_check()
