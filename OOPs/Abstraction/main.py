from abc import ABC, abstractmethod 

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side = side
    

class Circle(abstract):
    def __init__(self,radius):
        self.radius = radius
    
    def perimeter(self): 
        print("I created a perimeter")
    
    def area(self):
        print("I created area")

""" We nood to create abstract class method in child class of its"""

obj = Circle(6)