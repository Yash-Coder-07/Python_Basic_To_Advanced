class Animal:
    def __init__(self,name):
        pass
    
class Human:
    def __init__(self,name,age):
        pass

# which is written first in inheritance subclass access its properties
class Robots(Animal,Human):
    name3 = "Yash"

obj = Robots()