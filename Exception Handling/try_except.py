# a = int(input("Tell Your number:-"))

# try:
#     print(10/a)
# except Exception as err:
#     print(f"SOrry there is an err as {err}")
# # If except block run then else block will no run 
# # If except block not run then else block run
# else:
#     print("Good there is no exception")

# # finally block run any how no one can stop it 
# finally:
#     print("I will run no matter what")

# print("Ok i have done my division")

""" raise which manually throws exception
    when we try to raise error on own then execution of file is stopped so we use try 
"""

age = int(input("Tell your age : "))
try:
    if age <10 or age >18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")

except Exception as err:
    print(f"Error occured as {err}")

print("Club will start soon...")