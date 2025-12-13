# Print 1 to 30 in while loop
# a = 1
# while a<=30:
#     print(a)
#     a += 1


""" While Loop questions """

# Question Sperate each digit of numbe rand print it on new line
# n = 256
# while n>0:
#     print(n%10)
#     n = n//10 # floor division to remove value after decimal


# Question Reverse the number
# a = 256
# rev =0
# while a>0:
#     rev = rev *10 + a%10
#     a = a//10
# print(rev)

# Question number is palindrome or not

# n = 121
# copy = n
# rev =0
# while n>0:
#     rev = rev *10 + n%10
#     n = n//10
# if rev==copy:
#     print("Number is Palindrome")


# Question Generate random integer
import random

num = random.randint(1,10)
print(num)
guess = int(input("Guess your number : "))

if num==guess:
    print("You are right")
else:
    print("You are not  right")
