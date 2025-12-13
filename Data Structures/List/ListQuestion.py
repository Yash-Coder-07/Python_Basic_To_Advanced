# l = [-45,67,12,-68,-69,34]
# print("Positive element are")
# for i in l:
#     if(i>=0):
#         print(i)

# print("Negative element are")
# for i in l:
#     if(i<0):
#         print(i)


# Find mean of element
# l =[12,3,4,5,34,56,78,98,6]
# sum =0
# for i in l:
#     sum +=i
# print(sum//len(l))


# Greatest element
# l =[12,36,14,19,128,6,13]
# greatest =0
# for i in l:
#     if(greatest <i):
#         greatest = i
# print(f"Greatest element is {greatest}")

# Print second largets number
# l = [12,36,14,19,128,6,13]
# largest =l[0]
# second_largest =0
# for i in l:
#     if(i>largest):
#         second_largest = largest 
#         largest = i
#     elif(i<largest and i>second_largest):
#         second_largest = i
# print(largest)
# print(second_largest)


# Check if list is sorted or not
# l =[12,13,14,15]
# for i in range(len(l)-1):
#     if(l[i]<l[i+1]):
#         continue
#     else:
#         print("Not sorted list")
#         break
# # below else statement is linked with for loop 
# # if break statement is works then else will not work
# # otherwise sle of for loop will work
# else:
#     print("Your list is sorted")