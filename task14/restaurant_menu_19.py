# Write program for building restaurant menu using class in Python.
class Restaurant:
    def __init__(self):
        self.nonveg = {}
        self.veg = {}
        self.dessert = {}
    
    def addNon(self,name,rate):
        self.nonveg[name] = rate
        print(self.nonveg)

    def addVeg(self,name,rate):
        self.veg[name] = rate
        print(self.nonveg)

    def addDessert(self,name,rate):
        self.dessert[name] = rate
        print(self.nonveg)

    def removeDish(self, name):
        if name in self.nonveg:
            del self.nonveg[name]
        elif name in self.veg:
            del self.veg[name]
        elif name in self.dessert:
            del self.dessert[name]
        else:
            return None

    def displayAllDishes(self):
        print("\n*****Today's Special*****")
        print("***Non Veg***")
        for dish_name,rate in self.nonveg.items():
            print(f"{dish_name}  :  {rate}")
        print("***Veg***")
        for dish_name,rate in self.veg.items():
            print(f"{dish_name}  :  {rate}")
        print("***Dessert***")
        for dish_name,rate in self.dessert.items():
            print(f"{dish_name}  :  {rate}")

dish = Restaurant()
while True:
    print("\n1.Add Non Vegtarian Food")
    print("2.AddnVegtarian Food")
    print("3.Add Desserts")
    print("4.Remove")
    print("5.Display")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        dish_name = input("\nEnter the name of the dish:")
        rate = int(input("Enter the rate of the dish:"))
        dish.addNon(dish_name,rate)

    elif choice == 2:
        dish_name = input("\nEnter the name of the dish:")
        rate = int(input("Enter the rate of the dish:"))
        dish.addVeg(dish_name,rate)

    elif choice == 3:
        dish_name = input("\nEnter the name of the dish:")
        rate = int(input("Enter the rate of the dish:"))
        dish.addDessert(dish_name,rate)

    elif choice == 4:
        dish_name = input("\nEnter the name of the dish to be removed:")
        dish.removeDish(dish_name)
    
    elif choice == 5:
        dish.displayAllDishes()

    else:
        print("\nInvalid choice")
