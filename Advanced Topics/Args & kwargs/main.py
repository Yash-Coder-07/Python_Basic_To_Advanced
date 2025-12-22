# def addition(a,b):
#     print(a+b)

# addition(12,34)


""" Args single star is important....
use when multiple arguments are their 
return in Tuple data structure
"""


def decorator(func):
    def wrapper(*args,**kwargs):
        print("Your given number adition is : ")
        func(*args,**kwargs)
        print("Thank You....")
    return wrapper


@decorator
def addition(*args,**kwargs):
    sum =0
    for i in args:
        sum = sum + i
    print(f"sum is {sum}")

addition(12,12,13,78,98,6,5,4,7,8,2,152,2,5)


""" In kwargs double star is important
use when their is multiple key and value pair information
return in Dictionary Data Structure 
"""

# def information(**kwargs):
#     print("Your information is\n\n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")


# information(name ="Yash", age = 20, designation ="AI/ML Engineer")

