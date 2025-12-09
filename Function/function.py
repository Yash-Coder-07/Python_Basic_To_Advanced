# def hello():
#     print("Hello World")
# hello()


# def sum(a,b):
#     c = a+b
#     print(f"Sum of your numbers is: {c}")
# sum(5,6)


# def hello(name,age):
#     print(f"Your name is {name} and your age is {age}")

# Positional Argument Sequence of argument must be same
#hello("Yash","20") 

# Keyword Argument sequence of argument doesnt matter
#hello(age = 21, name ="Pranav") 

# Default Argument
# def sum(a,b=45):
#     print(f"The sum is {a+b}")

# sum(12) # No need to pass the b value 
# sum(12,34) # b value is override 
 
# String is palindrome or not

def palindrome(str):
    rev =""
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]
    
    if rev==str:
        print("Palindrome")
    else:
        print("Not Palindrome") 

palindrome("m adam")
palindrome("Yash")
palindrome("qwerrewq")