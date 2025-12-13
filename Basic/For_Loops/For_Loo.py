# For loop
# range(start,end,step)
# Deafult value of start = 0 and step = 1


#a = range(1,20,1)
#for i in a:
#    print(i)


#for i in range(0,20,2):
#    print(i)


#for i in range(50,19,-1):
#    print(i)

#a = "SHERIYANS"

#for i in range(0,9,1):
#    print(a[i])


#for i in a:
#    print(i)



# Break and continue

#for i in range(1,21):
#    if i==15:
#        continue
#    print(i)            


# if break works then else not works
# if break fails then else works
for i in range(1,21):
    if i==56:
        print("Break statement is executed")
        break
    print(i)

else:
    print("Break statement is not executed")