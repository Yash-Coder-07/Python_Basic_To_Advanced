class Animal:
    def __init__(self,name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"Helllo how are you your name is {self.name}"
    
    def __add__(self,other):
        sum = 0
        for i in other:
            sum =sum + i.age

        return f"Your sum of ages are {self.age+sum}"

obj = Animal("Lion",12)
obj2 = Animal("tiger",15)
obj3 = Animal("Leopard",20)
print(obj+(obj2,obj3))

""" for 3 object we need to pass 2 object as tuple in () parenthesis"""
