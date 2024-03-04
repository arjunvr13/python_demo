# Write a Python function called calculate_discounted_price that takes theoriginal price of an item 
# and a discount percentage as input. The function should return the discounted price after applying 
# the discount. Ensure that the function handles the case where the discount percentage is negative
# and raises a custom exception called InvalidDiscountError with an appropriate error message.
class InvalidDiscountError(Exception):
    def __init__(self,dis_percnt):
        self.dis_percnt = dis_percnt

    def __str__(self):
        return f"Negative amount the discount {self.dis_percnt}% must be invalid"
def calculate_discounted_price(price,dis_percnt):
    discount_amt = price - (price * dis_percnt)/100
    return discount_amt

price = int(input("Enter the price of the item purchased:"))
dis_percnt = int(input("Enter the discount in percentage(%):"))
result = calculate_discounted_price(price,dis_percnt)
try:
    if result < 0:
        raise InvalidDiscountError(dis_percnt)
    else:
        print("Payable Amount:",result)
except InvalidDiscountError as e:
    print(e)