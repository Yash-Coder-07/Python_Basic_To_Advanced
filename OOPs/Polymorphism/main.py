# Python overwrites a method 
# def show():
#     print("How are you")

# def show():
#     print("You are best")

# show()

""" ****************** PolyMorphism ***************** """
# Method overloading not exist in Python
# method Overriding
# if you have parent class and child class and same method name 
# then if object is calling a method then it calls child class method and parent class method get overwrites 

class Animal:
    def show(self):
        print("Hello I am Yash")
    
class Human(Animal):
    def show(self):
        print("How are you..?")

obj = Human()
obj.show()