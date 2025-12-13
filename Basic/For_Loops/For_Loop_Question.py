# Accept integer to and print hello world n times
#n = int(input("Enter the number"))
#for i in range(0,n,1):
#    print("HELLO WORLD")


# Question Take number as input and print its table
# n = int(input("Enter the number"))
# for i in range(1,11,1):
#     print(n*i)


# Question Factorila of n numbers
# n = int(input("Enter the number :"))
# fact=1
# for i in range(n,0,-1):
#     fact = fact*i
#print(f"Youa factorial is {fact}")


# Question find factor
# n = int(input("enter the number : "))
# end = int(n/2) +1
# for i in range(1,end,1):
#     if n%i==0:
#         print(i)
# print(n)


# Question number is perfect number or not
# n = int(input("Enter the number : "))
# end = int(n/2) +1
# sum = int(0)
# for i in range(1,end,1):
#     if n%i==0:
#         sum +=i
# print(sum)
# if sum == n:
#     print(f"Yes the number{n} is perfect number")
# else:
#     print(f"No the number{n} is perfect number")


# Question Number is prime or not
# n = int(input("Enter the number :"))
# end = int(n/2)+1
# count =0
# for i in range(2,end,1):
#     if n%i==0:
#         count=count+1
# if count==0:
#     print("Number is prime")
# else:
#     print("Number is not prime")


""" Question On the basis of String"""

# Question Reverse a string
# a = "SHERYIANS"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])


# Question Strng is palindrome or not   
# a = input("Enter the string :")
# b =""
# for i in range(len(a)-1,-1,-1):
#     b = b+a[i]

# if b==a:
#     print("Your string i splainrome")
# else:
#     print("Not palindrome")


# Question count of alphabet , digit, special character

# a = input("Enter the string :")
# char =0
# dig =0
# schar =0
# for i in a:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char +=1
#     else:
#         schar +=1
# print(f"Digit is {dig} special Character is {schar} and character is {char}")
