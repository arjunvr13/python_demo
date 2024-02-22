# Write a Python class, Square, and define two methods that return the square area and perimeter.
class Square:
    def area_square(self,a):
        print("Area of the square:",a**2)
    
    def perimeter_square(self,a):
        print("perimeter of the square:",4*a)

a = int(input("Enter the side of the square:"))
res = Square()
res.area_square(a)
res.perimeter_square(a)