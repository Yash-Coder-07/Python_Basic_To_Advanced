# l =[]
# for i in range(1,21):
#     if i%2==0:
#         l.append(i)
# print(l)


""" ******** For List ********"""
# first thing i need to append then loop then condition
# l=[i for i in range(1,21) if i%2==0]
# print(l)

""" **********For Dictionary********** """
# l ={i : i**2 for i in range(1,10)}
# print(l)


"""******* For Set *********"""
l ={x*x for x in range(1,10) if x%2==0}
print(l)