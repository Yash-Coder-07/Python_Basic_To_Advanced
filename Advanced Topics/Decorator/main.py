# class Animal:
#     @property
#     def show(self):
#         print("Hello how are you")

# obj = Animal()
# obj.show # no need to add parenthesis for execute above is decorator


# here func is parameter which takes the method on which decorator is used
# Here func is hello function
# def decorate(func):
#     def wrapper():
#         print("I will print myself before hello function")
#         func() # Call the hello function  
#         print("I will print after function")
    
#     return wrapper # return wrapper function

# @decorate
# def hello():
#     print("Hello I am Yash")

# hello()


# def decorate(func):
#     def wrapper(a,b):
#         print("Addition of your number is :")
#         func(a,b)
#         print("Thank You...")
#     return wrapper

# @decorate
# def add(a,b):
#     print(f"Addition of two number is {a+b}")

# add(5,8)

# def addition(a,b):
#     print(a+b)

# addition(12,34)

def addition(*args):
    sum =0
    for i in args:
        sum = sum + i
    return sum

print(addition(12,12,13,78,98,6,5,4,7,8,2,152,2,5))