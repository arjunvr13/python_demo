from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("redefine the method")
    
class Triangle(Shape):
    def __init__(self,breadth,height):
        self.breadth = breadth
        self.height = height

    def area(self):
        return 1/2*(self.breadth * self.height)
    

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side**2
    

class Pentagon(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return 0.25 * (5 * (5 + 2 * (5**0.5))) * self.side**2


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

s1 = Triangle(3,4)
print("Area of Triangle:",s1.area())
s2 = Square(4)
print("Area of Square:",s2.area())
s3 = Pentagon(4)
print("Area of Pentagon:",s3.area())
s4 = Circle(5)
print("Area of Circle:",s4.area())