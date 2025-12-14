class  Animal:
    name = "Lion" # class Attribute

    def __init__(self,age,type):
        self.age = age # instance attribute which is with self

    def show(self): # instance Method which is with self 
        print(f"Your animal is here {self.age}")    
    
    # below is class method we create it by using  decorator
    # @classmethod and pass cls instead of self
    @classmethod
    def hello(cls): # cls target class location
        print("Hello how are you ")
    

    @staticmethod
    def static():
        print("I am static method not targeting class and object")
    
obj = Animal(12)


