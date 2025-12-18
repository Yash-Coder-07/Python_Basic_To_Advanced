# below is acsess modifier in Python

# 1. Protected to implement this we add ( _ )at starting of Attributes and methods
# Example _a is now protected

""" It is not mainly use in Python but it use to tell user """
# class Factory:
#     _a ="Pune"

#     def _show(self):
#         print("Hello I am a Pune Factory")

# class Bhopal(Factory):
#     def show(self):
#         print(super()._a)

# obj = Bhopal()
# obj.show()


"""  ***************** Private Access Modifier ***************** """
# For this private access modifier we add 2 underscore infront of Attribute & Methods
# Example...(__) .... __a is now private and cannot access outside class

# class Factory:
#     __a ="Pune"

#     def __show(self):
#         print("Hello I am a Pune Factory")

# obj2 = Factory()
# obj2.__show() # This is not also accessible bcz i is outside class

""" To access above using private modifier """

class Factory:
    __a = "Pune"

    def show(self):
        print(Factory.__a)  # Access using class name but we cant change it
    
obj = Factory()
obj.show()

