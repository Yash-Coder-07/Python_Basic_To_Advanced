# class Factorymumbai: # PArent class / superclass
#     a = "I am attribute mentioned inside factory"     
#     def hello(self):
#         print("Hello I am method mentioned inside Factory")

# class FactoryPune(Factorymumbai): # child class / sub class
#     pass

# obj = Factorymumbai()
# #print(obj.a)
# #obj.hello()

# obj2 = FactoryPune()
# print(obj2.a)
# obj2.hello()

""" 
If child has its own __init__, parent __init__ is NOT automatic

Use super() to call parent constructor

Child method overrides parent method with same name
"""
class Animal:
    def __init__(self,name):
        self.name = name 
    
    def show(self):
        print(f"Hello your name is {self.name}")

# Child class alos has power of constructor of parent class
class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
    
    def show(self):
        print(f"Hello your name is {self.age}")

person1 = Human("Yash",20)
person1.show()

animal1 = Animal("Lion")
animal1.show()