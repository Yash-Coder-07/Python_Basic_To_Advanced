"""
1. List are Mutable...We can edit them
2. Duplicates are allowed in List 
3. They ar eHeterogenous nature 
   means we can save different type of data in one list like
   a=[3,5,6,7,8,9.45,print(),True]
4. We can acess list by index it store sequentially by user
"""


a = [12,13,14,15,12,1,12,45.5]

# First way using index
#for i in range(len(a)):
#    print(a[i])


# 2nd way is directly on values
# for i in a:
#     print(i)

#help(list)

l = [1,2,3,4,5,6]
l.append(6) # it add element at the last of list
print(l)

l.insert(3,3.5)
print(l)

l.extend([7,8,9]) # add element at the end but require as list
print(l)

l.remove(6) # First occurence of that value is remove only
print(l)
