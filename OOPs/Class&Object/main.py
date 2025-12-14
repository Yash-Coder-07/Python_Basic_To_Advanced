class Factory:
    a = 12   # Attribute
    
    def hello(self):     # Method
        print("How are you")
    
    print("Hello how are you I am getting initialized")

# Factory()

# Factory().hello() #accessing methods in class
# print(Factory().a)  #accessing attribute in class


""" ..........What is Object......r....."""
# here obj is now Object it has all power related to class
# When Python defines the class Factory, it executes everything 
# inside the class body immediately, except method bodies.
obj = Factory()
print(obj.a)
obj.hello()