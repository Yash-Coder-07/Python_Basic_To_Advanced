"""
Set are Mutable, Not allowed Duplicates
Sets are Unorderd, Set is Semi-Heterogenous 
It store some data types like numbers, string, tuples ,not list, not dictionaries
"""
# a ={1,2,8,9,"Hello",3,4,5,65}
# print(type(a))


# Set Traversing  it gives with random sequence
# for i in a:
#     print(i)


## Set Methods we can modify set by using set methods ...
# a ={1,2,3,4,5,6}
# a.remove(2)
# print(a)

# a.clear()...Remove all elements

""" Union and intersection of set"""

b ={1,2,3,4,5}
c ={3,4,5,6,7}

unionSet = b.union(c)
print(unionSet)

intersectionSet = b.intersection(c)
print(intersectionSet)

# b.()c gives difference of b element 
# c.()b gives difference of c element 
difference = b.difference(c) 
print(difference)


# symmetric_differnce gives total different element from both set
symmdiff = b.symmetric_difference(c)
print(symmdiff)

# This gives udated c with not intersection element
c =-b
print(c)