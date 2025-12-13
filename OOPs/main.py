class Factory:
    a = 12   # Attribute
    
    def hello(self):
        print("How are you")
    
    print("Hello how are you I am getting initialized")

Factory()

Factory().hello() #accessing methods in class
print(Factory().a)  #accessing attribute in class
